import os
import sys
import json
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
  sys.path.append(module_path)

from IPython.core.display import HTML
from functools import partial

from engine.utils import ProgramGenerator, ProgramInterpreter
from prompts.multichoice_tvp import create_prompt
from engine.video import Video
import pandas as pd
from tqdm import tqdm
import io, tokenize

import argparse
import numpy as np
from engine.ssparser import fix

parser = argparse.ArgumentParser(description='Run the video agent experiment')
parser.add_argument('--model', type=str, default='gpt', help='Model to generate the script')
args = parser.parse_args()

def parse_step(step_str,partial=False):
    tokens = list(tokenize.generate_tokens(io.StringIO(step_str).readline))
    output_var = tokens[0].string
    step_name = tokens[2].string
    parsed_result = dict(
        output_var=output_var,
        step_name=step_name)
    if partial:
        return parsed_result

    arg_tokens = [token for token in tokens[4:-3] if token.string not in [',','=']]
    num_tokens = len(arg_tokens) // 2
    args = dict()
    for i in range(num_tokens):
        args[arg_tokens[2*i].string] = arg_tokens[2*i+1].string
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

prompter = partial(create_prompt,method='all')
generator = ProgramGenerator(prompter=prompter, model_name_or_path=model)
interpreter = ProgramInterpreter()
import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key

module_list = [
    "LOC", "CLIP", "CLIP_BEFORE", "CLIP_AFTER", "CLIP_AROUND", "EVAL",
    "LENGTH", "VQA", "VIDQA", "CAP", "RESULT", 'SELECT'
]

dataset = pd.read_csv('dataset/NExTVideo/test.csv')
folder_name = f'results_vidagent_{args.model}_vqa_cap_ssparser'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for idx, row in tqdm(dataset.iterrows()):
    if idx < 327:
        continue
    if idx == 400:
        break
    # test my method
    question = row['question'].capitalize() + '?'
    print(question)
    video_id = row['video']
    answer = row['answer']
    print(video_id)
    print('choices:', row['a0'], row['a1'], row['a2'], row['a3'], row['a4'])
    print('reference answer:', answer)
    try:
        prog,_ = generator.generate(dict(question=question))
    except Exception as e:
        try:
            prog,_ = generator.generate(dict(question=question))
        except Exception as e:
            prog,_ = generator.generate(dict(question=question))
    print(prog)
    with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','w') as f:
        f.write(f'Question: {question}\n\n')
        f.write(f'Reference Answer: {answer}\n\n')
        f.write(f'Video ID: {row["video"]}\n\n')
        f.write(f'Original program:\n\n```\n{prog}\n```\n')
    init_state = dict(
        VIDEO=Video.read_file(f'dataset/NExTVideo/videos/{video_id}.mp4'),
        CHOICES=[row['a0'], row['a1'], row['a2'], row['a3'], row['a4']]
    )
    prog = fix(prog, question, module_list, init_state)
    prog = prog.replace('VIDQA', 'VQA')
    print(prog)
    with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
        f.write(f'Program:\n\n```\n{prog}\n```\n')
    prog_common = '\n'.join(prog.split('\n')[:-3])
    choices = str([row['a0'], row['a1'], row['a2'], row['a3'], row['a4']]).replace("'", " ")
    result, _, _ = interpreter.execute(f'ANSWERS0=VIDQA(video=VIDEO,question="{question} Analyze and select your choice among: {choices}")',init_state,inspect=True)
    print('vidqa:', result)
    try:
        if prog_common != '':
            result, prog_state, html_str = interpreter.execute(prog_common,init_state,inspect=True)
            with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
                f.write(f'Rationale common:\n\n{html_str}\n\n')
        else:
            prog_state = init_state
            with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
                f.write(f'Rationale common:\n\n\n\n')
        result_vqa, prog_state, html_str = interpreter.execute('\n'.join(prog.split('\n')[-3:]),prog_state,inspect=True)
        with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
            f.write(f'Rationale VQA:\n\n{html_str}\n\n')
        prob_vqa = prog_state['PROB']
        with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
            f.write(f'Prob_VQA: {prob_vqa}\n\n')
        changed_line = prog.split('\n')[-3]
        parse_result = parse_step(changed_line)
        output_var = parse_result['output_var']
        video_var = parse_result['args']['video']
        new_line = f'{output_var}=CAP(video={video_var})\n'
        result_cap, prog_state, html_str = interpreter.execute(new_line + '\n'.join(prog.split('\n')[-2:]),prog_state,inspect=True)
        with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
            f.write(f'Rationale CAP:\n\n{html_str}\n\n')
        prob_cap = prog_state['PROB']
        with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
            f.write(f'Prob_CAP: {prob_cap}\n\n')
        new_line = changed_line.replace('VQA', 'VIDQA') + '\n'
        result_vidqa, prog_state, html_str = interpreter.execute(new_line + '\n'.join(prog.split('\n')[-2:]),prog_state,inspect=True)
        with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
            f.write(f'Rationale VIDQA:\n\n{html_str}\n\n')
        prob_vidqa = prog_state['PROB']
        with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
            f.write(f'Prob_VIDQA: {prob_vidqa}\n\n')
        max_norm_prob_vqa = max(prob_vqa.values()) / sum(prob_vqa.values())
        max_norm_prob_cap = max(prob_cap.values()) / sum(prob_cap.values())
        max_norm_prob_vidqa = max(prob_vidqa.values()) / sum(prob_vidqa.values())
        max_norm_idx = [max_norm_prob_vqa, max_norm_prob_cap, max_norm_prob_vidqa]
        result_idx = np.argmax(max_norm_idx)
        result = [result_vqa, result_cap, result_vidqa][result_idx]
    except Exception as e:
        choices = [row['a0'], row['a1'], row['a2'], row['a3'], row['a4']]
        result, _, _ = interpreter.execute(f'ANSWERS0=VIDQA(video=VIDEO,question="{question}")\nANSWER0=SELECT(question="{question}",information=ANSWERS0,choices=CHOICES)\nFINAL_RESULT=RESULT(var=ANSWER0)',prog_state,inspect=True)
    print(result)
    with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
        f.write(f'Answer: {result}\n\n')