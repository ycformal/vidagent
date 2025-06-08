import os
os.environ["HF_HOME"] = "/home/hice1/yxu846/scratch/models"

import sys
import ast
import numpy as np
import pandas as pd
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import torch
import torch.nn.functional as F

# ─── Settings ────────────────────────────────────────────────────────────────
DATA_CSV     = 'dataset/NExTVideo/test.csv'
RESULTS_DIR  = 'results_vidagent_gpt_vqa_cap_ssparser'
MAX_SAMPLES  = 400      # as in your original break
EMB_MODEL    = "hkunlp/instructor-xl"
LR           = 0.1
EPOCHS       = 200

# ─── Helpers ──────────────────────────────────────────────────────────────────
def analyze_distribution(prob_dist):
    total = sum(prob_dist.values())
    max_key = max(prob_dist, key=prob_dist.get)
    max_val = prob_dist[max_key]
    return max_key, (max_val / total) if total > 0 else 0.0

def load_and_parse(max_samples=MAX_SAMPLES):
    """
    Reads your CSV and corresponding .md files, extracts:
      - ratios:   [N,3] of max_prob/total_prob
      - keys:     [N,3] of the chosen string per source
      - choices:  [N,5] of choice strings
      - answers:  [N]   of correct answer indices (0–4)
    """
    df = pd.read_csv(DATA_CSV)
    ratios   = []
    keys     = []
    choices  = []
    answers  = []
    for idx, row in tqdm(df.iterrows(), total=len(df)):
        if idx >= max_samples:
            break
        question = row['question'].capitalize() + '?'
        vid      = row['video']
        md_path  = f"{RESULTS_DIR}/{question.replace(' ', '_')}_{vid}.md"

        with open(md_path, 'r') as f:
            content = f.read()

        P_vqa   = ast.literal_eval(content.split('Prob_VQA: ')[1].split('\n')[0])
        P_cap   = ast.literal_eval(content.split('Prob_CAP: ')[1].split('\n')[0])
        P_vidqa = ast.literal_eval(content.split('Prob_VIDQA: ')[1].split('\n')[0])

        k1, r1 = analyze_distribution(P_vqa)
        k2, r2 = analyze_distribution(P_cap)
        k3, r3 = analyze_distribution(P_vidqa)

        ratios.append([r1, r2, r3])
        keys.append([k1, k2, k3])
        cands = [row[f'a{i}'] for i in range(5)]
        choices.append(cands)
        answers.append(int(row['answer']))

    return ratios, keys, choices, answers

# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # 1) Load & parse data
    ratios_list, keys_list, choices_list, answers_list = load_and_parse()
    N = len(ratios_list)

    # 2) Device & embedder setup
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    embedder = SentenceTransformer(EMB_MODEL, device=device)

    # Flatten for one‐shot encoding
    flat_keys    = [k for sample in keys_list   for k in sample]   # N*3
    flat_choices = [c for sample in choices_list for c in sample] # N*5

    # Encode to tensors on correct device
    all_key_embs    = embedder.encode(flat_keys,    batch_size=64, convert_to_tensor=True, device=device)  # (N*3, D)
    all_choice_embs = embedder.encode(flat_choices, batch_size=64, convert_to_tensor=True, device=device)  # (N*5, D)

    D = all_key_embs.size(1)
    # Reshape to [N,3,D] and [N,5,D]
    key_embs    = all_key_embs.view(N, 3, D)
    choice_embs = all_choice_embs.view(N, 5, D)

    # Normalize embeddings
    key_embs_norm    = F.normalize(key_embs,    p=2, dim=2)
    choice_embs_norm = F.normalize(choice_embs, p=2, dim=2)

    # Prepare ratio & answer tensors on same device
    ratios_tensor  = torch.tensor(ratios_list, dtype=torch.float, device=device)  # (N,3)
    answers_tensor = torch.tensor(answers_list, dtype=torch.long, device=device)   # (N,)

    # 3) Define learnable weights
    raw_w     = torch.nn.Parameter(torch.zeros(3, device=device), requires_grad=True)
    optimizer = torch.optim.Adam([raw_w], lr=LR)
    loss_fn   = torch.nn.CrossEntropyLoss()

    # 4) Training loop
    for epoch in range(1, EPOCHS+1):
        optimizer.zero_grad()

        w = F.softmax(raw_w, dim=0)                              # (3,)
        weight_ratio = (w.unsqueeze(0) * ratios_tensor).unsqueeze(-1)  # (N,3,1)

        # Compute cosine sims: (N,3,5)
        sims = torch.einsum('nkd,njd->nkj', key_embs_norm, choice_embs_norm)

        # Combine weighted sims into logits: (N,5)
        logits = (weight_ratio * sims).sum(dim=1)

        loss = loss_fn(logits, answers_tensor)
        loss.backward()
        optimizer.step()

        if epoch % 20 == 0 or epoch == 1:
            with torch.no_grad():
                preds = logits.argmax(dim=1)
                acc = (preds == answers_tensor).float().mean().item()
            print(f"Epoch {epoch:03d} — loss: {loss.item():.4f}, acc: {acc:.4f}")

    # 5) Final evaluation (on same device)
    with torch.no_grad():
        w_final_tensor = F.softmax(raw_w, dim=0)                     # (3,) on device
        wr             = (w_final_tensor.unsqueeze(0) * ratios_tensor).unsqueeze(-1)  # (N,3,1)
        sims           = torch.einsum('nkd,njd->nkj', key_embs_norm, choice_embs_norm)  # (N,3,5)
        logits_eval    = (wr * sims).sum(dim=1)                       # (N,5)
        preds_eval     = logits_eval.argmax(dim=1)
        final_acc      = (preds_eval == answers_tensor).float().mean().item()
        w_final        = w_final_tensor.cpu().numpy()

    print(f"\n→ Learned weights: {w_final}")
    print(f"→ Final accuracy on {N} samples: {final_acc:.4f}")
