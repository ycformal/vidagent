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
interpreter = ProgramInterpreter(method = 'agent')
import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key

dataset = pd.read_csv('dataset/NExTVideo/test.csv')
folder_name = f'results_vlm_qwen_open_ended_16'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for idx, row in tqdm(dataset.iterrows()):
    if idx < 400:
        continue
    # test my method
    question = row['question'].capitalize() + '?'
    print(question)
    video_id = row['video']
    answer = row['answer']
    print(video_id)
    print('choices:', row['a0'], row['a1'], row['a2'], row['a3'], row['a4'])
    print('reference answer:', answer)
    with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','w') as f:
        f.write(f'Question: {question}\n\n')
        f.write(f'Reference Answer: {answer}\n\n')
        f.write(f'Video ID: {row["video"]}\n\n')
    init_state = dict(
        QUESTION=question,
        VIDEO=Video.read_file(f'dataset/NExTVideo/videos/{video_id}.mp4'),
        CHOICES=[row['a0'], row['a1'], row['a2'], row['a3'], row['a4']]
    )
    choices = [row['a0'], row['a1'], row['a2'], row['a3'], row['a4']]
    result, _ = interpreter.execute(f'ANSWERS0=VIDQA(video=VIDEO,question="{question}")\nSELECTED=SELECT(question="{question}",information=ANSWERS0,choices=CHOICES)'.replace("'", " "),init_state)
    print(result)
    with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
        f.write(f'Answer: {result}\n\n')