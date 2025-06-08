#!/usr/bin/env python
# run_nextqa.py ─────────────────────────────────────────────────────────────
"""
Zero‑shot evaluation of a SeViLA‑style Video‑QA model on NeXT‑QA.

All checkpoints, tokenizer files, timm weights, etc. are cached under
    /home/hice1/yxu846/scratch/models
so repeated runs (and other scripts) reuse the same downloads.

Requirements
------------
pip install torch torchvision lavis decord pandas tqdm
"""
# ──────────────────── force cache dir *before* heavy imports ───────────── #
import os, pathlib
CACHE_DIR = pathlib.Path("/home/hice1/yxu846/scratch/models")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

# Hugging Face Transformers / datasets
os.environ["HF_HOME"] = str(CACHE_DIR)
os.environ["TRANSFORMERS_CACHE"] = str(CACHE_DIR / "transformers")
# timm / torch.hub
os.environ["TORCH_HOME"] = str(CACHE_DIR / "torch_hub")
# LAVIS (uses "LAVIS_CACHE" if provided; falls back to TORCH_HOME otherwise)
os.environ["LAVIS_CACHE"] = str(CACHE_DIR / "lavis")

# ──────────────────────────── imports ──────────────────────────────────── #
import warnings, logging, argparse
from typing import List, Dict

import torch, torchvision.transforms as T
from torch import nn
from torch.utils.data import Dataset, DataLoader
from decord import VideoReader, cpu
import pandas as pd
from tqdm import tqdm
from lavis.models import load_model_and_preprocess                 # BLIP‑2

warnings.filterwarnings("ignore")
logging.basicConfig(format="%(asctime)s | %(levelname)s | %(message)s",
                    level=logging.INFO)

# ────────────────────────── Dataset loader ────────────────────────────── #
class NeXTQADataset(Dataset):
    def __init__(self, csv_path: str, video_dir: str,
                 num_frames: int = 8, img_size: int = 224):
        self.df = pd.read_csv(csv_path)
        self.video_dir = pathlib.Path(video_dir)
        self.num_frames = num_frames
        self.transform = T.Compose([
            T.Resize(img_size, antialias=True),       # works on tensors
            T.CenterCrop(img_size),
            T.ConvertImageDtype(torch.float32),       # uint8 → float32, /255
            T.Normalize(mean=[0.48145466, 0.4578275, 0.40821073],
                        std=[0.26862954, 0.26130258, 0.27577711]),
        ])

    def __len__(self): return len(self.df)

    def _sample_indices(self, vr: VideoReader) -> List[int]:
        tot = len(vr)
        if tot <= self.num_frames:
            return list(range(tot)) + [tot-1]*(self.num_frames-tot)
        step = tot / self.num_frames
        return [int(i*step) for i in range(self.num_frames)]

    def __getitem__(self, idx):
        row = self.df.iloc[idx]

        # Some splits store the file name in different columns — try a few
        vid_key = "video" if "video" in row else ("vid" if "vid" in row else None)
        if vid_key is None:
            raise KeyError("Cannot find a 'video' or 'vid' column in the CSV.")

        # cast to str and add extension if missing
        video_fname = str(row[vid_key])
        if not video_fname.endswith(".mp4"):
            video_fname += ".mp4"

        vid_path = self.video_dir / video_fname            # <— no TypeError now
        vr = VideoReader(str(vid_path), ctx=cpu(0))

        frames = vr.get_batch(self._sample_indices(vr))    # T,H,W,C
        frames = frames.permute(0, 3, 1, 2)                # T,C,H,W
        frames = torch.stack([self.transform(f) for f in frames])

        options = [row[f"a{i}"] for i in range(5)]
        return {
            "video": frames,
            "question": row["question"],
            "options": options,
            "answer": row["answer"],
            "qid": idx,
            "video_file": video_fname,
        }


def collate_fn(batch: List[Dict]):
    max_t = max(item["video"].size(0) for item in batch)
    vids = []
    for item in batch:
        v = item["video"]
        if v.size(0) < max_t:
            pad = v[-1:].repeat(max_t - v.size(0), 1, 1, 1)
            v = torch.cat([v, pad])
        vids.append(v)
    vids = torch.stack(vids)                                # B,T,C,H,W
    return dict(
        video=vids,
        question=[b["question"] for b in batch],
        options=[b["options"]  for b in batch],
        answer=[b["answer"]    for b in batch],
        qid=[b["qid"]          for b in batch],
        video_file=[b["video_file"] for b in batch],
    )

# ───────────────────── prompt helper functions ────────────────────────── #
LOC_PROMPT = ("Does the information within the frame provide "
              "necessary details to accurately answer the question?")
QA_PROMPT  = ("Considering information in frames, select the correct "
              "answer from the options.")

def loc_input(q: str) -> str:                      return f"{q} {LOC_PROMPT}"
def qa_input(q: str, opts: List[str]) -> str:
    opt_txt = " ".join([f"{chr(65+i)}: {o}." for i,o in enumerate(opts)])
    return f"{q} {opt_txt} {QA_PROMPT}"

# ───────────────────── SeViLA architecture from BLIP‑2 ────────────────── #
class SeViLA_from_BLIP2(nn.Module):
    def __init__(self, device="cuda", frame_num=8):
        super().__init__()
        self.device = torch.device(device)
        # load BLIP‑2 (pre‑trained only)
        blip2, _, _ = load_model_and_preprocess(
            name="blip2_t5", model_type="pretrain_flant5xl",
            is_eval=True, device=self.device)

        # Vision encoder (frozen)
        self.visual_encoder = blip2.visual_encoder
        self.visual_encoder.eval()
        self.ln_vision      = blip2.ln_vision
        self.ln_vision_loc  = blip2.ln_vision.__class__(
            blip2.ln_vision.normalized_shape).to(self.device)
        self.ln_vision_loc.load_state_dict(blip2.ln_vision.state_dict())
        for p in self.visual_encoder.parameters(): p.requires_grad = False

        # Q‑Formers
        self.Qformer_ans      = blip2.Qformer
        self.query_tokens_ans = blip2.query_tokens
        from copy import deepcopy
        self.Qformer_loc      = deepcopy(blip2.Qformer)
        self.query_tokens_loc = nn.Parameter(
            blip2.query_tokens.data.clone(), requires_grad=False)
        for m in [self.Qformer_ans, self.Qformer_loc]:
            for p in m.parameters(): p.requires_grad = False

        # Projections
        self.t5_proj_ans = blip2.t5_proj
        self.t5_proj_loc = nn.Linear(*blip2.t5_proj.weight.T.shape, bias=False)
        self.t5_proj_loc.to(self.device)
        self.t5_proj_loc.weight.data = blip2.t5_proj.weight.data.clone()

        # Flan‑T5 (frozen)
        self.t5_model     = blip2.t5_model
        self.t5_tokenizer = blip2.t5_tokenizer

        # misc constants
        self.frame_num   = frame_num
        self.max_txt_len = 77
        self.answer_id   = [71, 272, 205, 309, 262]  # A‑E
        self.yes_id, self.no_id = 4273, 150
        ids_answer = [71, 272, 205, 309, 262]          # A‑E
        ids_bool   = [4273, 150]  
        print("Answer‑choice tokens:", self.t5_tokenizer.convert_ids_to_tokens(ids_answer))
        print("Yes/No tokens       :", self.t5_tokenizer.convert_ids_to_tokens(ids_bool))
        self.frame_prefix = ["Frame: "]
        self.vid_prefix   = [f"Frame {i+1}: " for i in range(frame_num)]
        self.ans_map      = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

    # ───────────────────────── generate ────────────────────────── #
    @torch.no_grad()
    def generate(self, samples: Dict):
        video   = samples["video"].to(self.device)             # B,T,C,H,W
        B, T, C, H, W = video.shape
        images  = video.view(-1, C, H, W)                      # BT,C,H,W

        # ViT
        with torch.cuda.amp.autocast(dtype=torch.bfloat16):
            img_embed = self.visual_encoder(images)            # BT,N,D
        N, D = img_embed.shape[1:3]
        img_att = torch.ones(img_embed.shape[:-1],
                             dtype=torch.long, device=self.device)

        # 1) Localiser branch
        loc_embed = self.ln_vision_loc(img_embed)
        qt_loc = self.query_tokens_loc.expand(img_embed.size(0), -1, -1)
        loc_out = self.Qformer_loc.bert(
            query_embeds=qt_loc, encoder_hidden_states=loc_embed,
            encoder_attention_mask=img_att, return_dict=True)
        loc_proj = self.t5_proj_loc(loc_out.last_hidden_state)       # BT,Q,H
        atts_loc = torch.ones(loc_proj.size()[:-1], dtype=torch.long,
                              device=self.device)

        prefix = self.t5_tokenizer(self.frame_prefix, add_special_tokens=False,
                                   truncation=True, max_length=self.max_txt_len,
                                   return_tensors="pt").to(self.device)
        prefix_ids   = prefix.input_ids.repeat(img_embed.size(0), 1)
        prefix_masks = prefix.attention_mask.repeat(img_embed.size(0), 1)
        prefix_emb   = self.t5_model.encoder.embed_tokens(prefix_ids)

        loc_tok = self.t5_tokenizer(samples["loc_input"], padding="longest",
                                    truncation=True, max_length=self.max_txt_len,
                                    return_tensors="pt").to(self.device)
        loc_ids   = loc_tok.input_ids.repeat_interleave(T, 0)
        loc_masks = loc_tok.attention_mask.repeat_interleave(T, 0)
        loc_emb   = self.t5_model.encoder.embed_tokens(loc_ids)

        enc_in  = torch.cat([prefix_emb, loc_proj, loc_emb], dim=1)
        enc_att = torch.cat([prefix_masks, atts_loc, loc_masks], dim=1)

        out_loc = self.t5_model.generate(
            inputs_embeds=enc_in, attention_mask=enc_att,
            do_sample=False, num_beams=1, max_new_tokens=1,
            return_dict_in_generate=True, output_scores=True)
        score_loc = out_loc.scores[0][:, self.yes_id].view(B, T)      # B,T
        top_idx   = torch.topk(score_loc, self.frame_num, dim=-1).indices
        top_idx_sorted = [sorted(lst.tolist()) for lst in top_idx]

        # 2) Answerer branch
        ans_embed = self.ln_vision(img_embed).view(B, T, N, D)
        sel_frames = torch.stack(
            [ans_embed[b, idx] for b, idx in enumerate(top_idx_sorted)]
        )                                                       # B,k,N,D
        sel_frames = sel_frames.view(B*self.frame_num, N, D)
        atts_sel   = torch.ones(sel_frames.shape[:-1],
                                dtype=torch.long, device=self.device)

        qt_ans = self.query_tokens_ans.expand(sel_frames.size(0), -1, -1)
        ans_out = self.Qformer_ans.bert(
            query_embeds=qt_ans, encoder_hidden_states=sel_frames,
            encoder_attention_mask=atts_sel, return_dict=True)
        ans_proj = self.t5_proj_ans(ans_out.last_hidden_state)       # Bk,Q,H
        ans_proj = ans_proj.view(B, self.frame_num, -1, ans_proj.size(-1))
        atts_ans = torch.ones(ans_proj.size()[:-1], dtype=torch.long,
                              device=self.device)

        vp_tok = self.t5_tokenizer(self.vid_prefix, add_special_tokens=False,
                                   truncation=True, max_length=self.max_txt_len,
                                   return_tensors="pt").to(self.device)
        vp_ids   = vp_tok.input_ids.unsqueeze(0).repeat(B, 1, 1)
        vp_masks = vp_tok.attention_mask.unsqueeze(0).repeat(B, 1, 1)
        vp_emb   = self.t5_model.encoder.embed_tokens(vp_ids)

        ans_proj = torch.cat([vp_emb, ans_proj], dim=2)
        atts_ans = torch.cat([vp_masks, atts_ans], dim=2)
        ans_proj = ans_proj.view(B, -1, ans_proj.size(-1))
        atts_ans = atts_ans.view(B, -1)

        qa_tok = self.t5_tokenizer(samples["qa_input"], padding="longest",
                                   truncation=True, max_length=self.max_txt_len,
                                   return_tensors="pt").to(self.device)
        qa_emb  = self.t5_model.encoder.embed_tokens(qa_tok.input_ids)
        enc_in2 = torch.cat([ans_proj, qa_emb], dim=1)
        enc_att2= torch.cat([atts_ans, qa_tok.attention_mask], dim=1)

        out_ans = self.t5_model.generate(
            inputs_embeds=enc_in2, attention_mask=enc_att2,
            do_sample=False, num_beams=1, max_new_tokens=1,
            return_dict_in_generate=True, output_scores=True)
        logits  = out_ans.scores[0][:, self.answer_id]                 # B,5
        pred    = torch.argmax(logits, dim=-1)                        # tensor

        return dict(
            prediction=pred.cpu().tolist(),
            answer=[
                self.ans_map[a] if isinstance(a, str) and a in self.ans_map else int(a)
                for a in samples["qa_output"]
            ],
            frame_idx=top_idx_sorted,
        )

def build_model(device="cuda"):
    m = SeViLA_from_BLIP2(device=device).to(device)
    m.eval()
    return m

# ───────────────────────────── eval loop ─────────────────────────────── #
@torch.no_grad()
def evaluate(model, loader, device, csv_out: pathlib.Path):
    records, correct, total = [], 0, 0
    for batch in tqdm(loader, ncols=80, desc="Infer"):
        loc_in = [loc_input(q) for q in batch["question"]]
        qa_in  = [qa_input(q, o) for q, o in zip(batch["question"], batch["options"])]

        output = model.generate(dict(
            video=batch["video"].to(device),
            loc_input=loc_in,
            qa_input=qa_in,
            qa_output=batch["answer"],
        ))
        preds, gts = output["prediction"], output["answer"]

        # store all info
        for i in range(len(preds)):
            rec = dict(
                qid=batch["qid"][i],
                video=batch["video_file"][i],
                question=batch["question"][i],
                a0=batch["options"][i][0],
                a1=batch["options"][i][1],
                a2=batch["options"][i][2],
                a3=batch["options"][i][3],
                a4=batch["options"][i][4],
                prediction=preds[i],   # 0‑4
                answer=gts[i],         # 0‑4
                result=preds[i],
                correct=int(preds[i]==gts[i]),
            )
            records.append(rec)
            correct += rec["correct"]
            total   += 1

    df = pd.DataFrame(records)
    df.to_csv(csv_out, index=False)
    logging.info(f"Saved predictions to {csv_out}")

    return correct / total

# ───────────────────────────────── main ───────────────────────────────── #
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv",    default="dataset/NExTVideo/test.csv")
    parser.add_argument("--videos", default="dataset/NExTVideo/videos")
    parser.add_argument("--out",    default="predictions_nextqa_sevila.csv",
                        help="path to save detailed csv")
    parser.add_argument("--batch_size", type=int, default=2)
    parser.add_argument("--num_workers", type=int, default=4)
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    ds  = NeXTQADataset(args.csv, args.videos)
    dl  = DataLoader(ds, batch_size=args.batch_size, shuffle=False,
                     num_workers=args.num_workers, collate_fn=collate_fn)
    model = build_model(device)

    acc = evaluate(model, dl, device,
                   csv_out=pathlib.Path(args.out).expanduser())
    print(f"\nNeXT‑QA zero‑shot accuracy: {acc*100:.2f}% "
          f"({int(acc*len(ds))}/{len(ds)})")

if __name__ == "__main__":
    main()
