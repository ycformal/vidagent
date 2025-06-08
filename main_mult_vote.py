import os
import sys
import json
import copy
from concurrent.futures import ThreadPoolExecutor

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from IPython.core.display import HTML
from functools import partial

from engine.utils import ProgramGenerator, ProgramInterpreter
from prompts.multichoice_tvp_multiple_questions import create_prompt
from engine.video import Video
from engine.visualizer import visualize
import pandas as pd
from tqdm import tqdm
import io, tokenize
from io import BytesIO
import base64

import argparse
import numpy as np
from engine.ssparser import fix
from sentence_transformers import SentenceTransformer, util
import torch
import openai
import threading

# ─── Argparse and setup ────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description='Run the video agent experiment')
parser.add_argument('--model', type=str, default='gpt', help='Model to generate the script')
args = parser.parse_args()

def parse_step(step_str, partial=False):
    tokens = list(tokenize.generate_tokens(io.StringIO(step_str).readline))
    output_var = tokens[0].string
    step_name = tokens[2].string
    parsed_result = dict(output_var=output_var, step_name=step_name)
    if partial:
        return parsed_result
    arg_tokens = [t for t in tokens[4:-3] if t.string not in {',', '='}]
    args = {arg_tokens[2*i].string: arg_tokens[2*i+1].string
            for i in range(len(arg_tokens)//2)}
    parsed_result['args'] = args
    return parsed_result

model = None
if args.model == 'gpt':
    model = 'gpt-3.5-turbo-instruct'
elif args.model == 'llama':
    model = 'meta-llama/Meta-Llama-3-8B'
elif args.model == 'glm':
    model = 'THUDM/glm-4-9b-hf'
elif args.model == 'mistral':
    model = 'mistralai/Mistral-Small-24B-Base-2501'
else:
    raise ValueError('Invalid model name')

prompter    = partial(create_prompt, method='all')
generator   = ProgramGenerator(prompter=prompter, model_name_or_path=model)
interpreter = ProgramInterpreter()

# decode OpenAI key
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join(chr(ord(k)-1) for k in key)
openai.api_key = key

module_list = [
    "LOC", "CLIP", "CLIP_BEFORE", "CLIP_AFTER", "CLIP_AROUND", "EVAL",
    "LENGTH", "VQA", "VIDQA", "CAP", "RESULT", "SELECT", "FLAG"
]

dataset     = pd.read_csv('dataset/NExTVideo/test.csv')
folder_name = f'results_vidagent_{args.model}_all_multi_question'
os.makedirs(folder_name, exist_ok=True)

_model = SentenceTransformer("hkunlp/instructor-xl")

def analyze_distribution(prob_dist):
    total   = sum(prob_dist.values())
    max_key = max(prob_dist, key=prob_dist.get)
    max_val = prob_dist[max_key]
    return max_key, max_val / total if total != 0 else 0

def vote(weights, ratios, keys, choices):
    scores       = [w * r for w, r in zip(weights, ratios)]
    best_source  = max(range(len(scores)), key=lambda i: scores[i])
    selected_key = keys[best_source]
    key_emb      = _model.encode(selected_key, convert_to_tensor=True)
    choice_embs  = _model.encode(choices, convert_to_tensor=True)
    sims         = util.cos_sim(key_emb, choice_embs)[0]
    return int(sims.argmax())

# --- NEW: clone_state to deep-copy tensors on the same device ---
def clone_state(state):
    new = {}
    for k, v in state.items():
        if isinstance(v, torch.Tensor):
            new[k] = v.clone()
        else:
            new[k] = copy.deepcopy(v)
    return new

def is_same(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False

# ─── Main loop ─────────────────────────────────────────────────────────────────
for idx, row in tqdm(dataset.iterrows(), total=len(dataset)):
    if idx < 1062:
        continue
    question = row['question'].capitalize() + '?'
    video_id = row['video']
    choices  = [row[f'a{i}'] for i in range(5)]
    answer   = row['answer']
    md_path  = f'{folder_name}/{question.replace(" ", "_")}_{video_id}.md'

    # nested try/except for generation
    try:
        prog, _ = generator.generate(dict(question=question))
    except Exception:
        try:
            prog, _ = generator.generate(dict(question=question))
        except Exception:
            prog, _ = generator.generate(dict(question=question))

    print(question, video_id)
    print('choices:', ', '.join(choices), 'reference answer:', answer)
    print(prog)

    # write header + original program
    with open(md_path, 'w') as f:
        f.write(f'Question: {question}\n\n')
        f.write(f'Reference Answer: {answer}\n\n')
        f.write(f'Video ID: {video_id}\n\n')
        f.write('Original program:\n\n```\n' + prog + '\n```\n\n')

    # fix program and write
    init_state = {
        "QUESTION": question,
        "VIDEO": Video.read_file(f'dataset/NExTVideo/videos/{video_id}.mp4'),
        "CHOICES": choices
    }
    prog = fix(prog, question, module_list, init_state).replace('VIDQA', 'VQA')
    print(prog)
    with open(md_path, 'a') as f:
        f.write('Program:\n\n```\n' + prog + '\n```\n\n')

    # execute common prefix exactly once
    lines       = prog.split('\n')
    prog_common = '\n'.join(lines[:-1]).strip()
    if prog_common:
        _, prog_state, html_common = interpreter.execute(prog_common, init_state, inspect=True)
    else:
        prog_state = init_state


    # snapshot common_state for branching
    common_state = clone_state(prog_state)

    # prepare branch snippets
    snippet_vqa   = lines[-1]
    pr            = parse_step(snippet_vqa)
    out_var, vid_var = pr['output_var'], pr['args']['video']
    snippet_cap   = f'{out_var}=CAP(video={vid_var})'
    snippet_vidqa = snippet_vqa.replace('VQA','VIDQA')

    snippet_vqa += f'\nSELECTED=SELECT(question="{question}",information=ANSWERS0,choices=CHOICES)'
    snippet_cap += f'\nSELECTED=SELECT(question="{question}",information=ANSWERS0,choices=CHOICES)'
    snippet_vidqa += f'\nSELECTED=SELECT(question="{question}",information=ANSWERS0,choices=CHOICES)'

    try:
        # run branches in parallel, reusing the same common_state structure
        def run_branch(code):
            state = clone_state(common_state)
            return interpreter.execute(code, state, inspect=True)

        with ThreadPoolExecutor(max_workers=3) as ex:
            fv   = ex.submit(run_branch, snippet_vqa)
            fc   = ex.submit(run_branch, snippet_cap)
            fvid = ex.submit(run_branch, snippet_vidqa)

            _, state_vqa,   html_vqa   = fv.result()
            _, state_cap,   html_cap   = fc.result()
            _, state_vidqa, html_vidqa = fvid.result()

        prob_vqa   = state_vqa['PROB']
        prob_cap   = state_cap['PROB']
        prob_vidqa = state_vidqa['PROB']

        # voting logic unchanged
        kv, rv     = analyze_distribution(prob_vqa)
        kc, rc     = analyze_distribution(prob_cap)
        kvid, rvid = analyze_distribution(prob_vidqa)

        if prob_vidqa[kvid] >= 40:
            predicted = vote([1],   [rvid],    [kvid],    choices)
        else:
            if kv != kvid and kc != kvid or is_same([prob_vidqa[key] for key in prob_vidqa.keys()]):
                predicted = vote([1,1,1],[rv, rc, rvid],[kv, kc, kvid],choices)
            else:
                predicted = vote([1],   [rvid],    [kvid],    choices)

        result = predicted

        text = f"""VIDQA branch: {prob_vidqa}
        VQA branch: {prob_vqa}
        CAP branch: {prob_cap}
        Answer: {choices[result]}"""
        vis_img = visualize(prog_common, prog_state, text)
        with BytesIO() as buffer:
            vis_img.save(buffer, 'jpeg')
            base64_img = base64.b64encode(buffer.getvalue()).decode()
        vis_img_html = f'<img style="vertical-align:middle" src="data:image/jpeg;base64,{base64_img}">'

        with open(md_path, 'a') as f:
            f.write(f'Visualization: \n\n{vis_img_html}\n\n')
            f.write(f'State VQA: {state_vqa}\n\n')
            f.write(f'Prob_VQA: {prob_vqa}\n\n')
            f.write(f'State CAP: {state_cap}\n\n')
            f.write(f'Prob_CAP: {prob_cap}\n\n')
            f.write(f'State VIDQA: {state_vidqa}\n\n')
            f.write(f'Prob_VIDQA: {prob_vidqa}\n\n')

    except Exception:
        # fallback unchanged
        result, _, _ = interpreter.execute(
            f'ANSWERS0=VIDQA(video=VIDEO,question="{question}")\n'
            f'ANSWER0=SELECT(question="{question}",information=ANSWERS0,choices=CHOICES)\n'
            f'FINAL_RESULT=RESULT(var=ANSWER0)',
            prog_state, inspect=True
        )

    print(result)
    with open(md_path, 'a') as f:
        f.write(f'Answer: {result}\n\n')
