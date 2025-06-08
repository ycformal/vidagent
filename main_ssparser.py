import os
import sys
import json
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
  sys.path.append(module_path)

from IPython.core.display import HTML
from functools import partial

from engine.utils import ProgramGenerator, ProgramInterpreter
from prompts.multichoice_tvp_multiple_questions import create_prompt
from engine.video import Video
import pandas as pd
from tqdm import tqdm
from engine.ssparser import fix

import argparse

parser = argparse.ArgumentParser(description='Run the video agent experiment')
parser.add_argument('--model', type=str, default='gpt', help='Model to generate the script')
args = parser.parse_args()

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

prompter = partial(create_prompt)
generator = ProgramGenerator(prompter=prompter, model_name_or_path=model)
interpreter = ProgramInterpreter()
import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key

module_list = [
    "LOC", "CLIP", "CLIP_BEFORE", "CLIP_AFTER", "CLIP_AROUND", "EVAL",
    "LENGTH", "VQA", "VIDQA", "CAP", "RESULT", 'SELECT', 'FLAG'
]

dataset = pd.read_csv('dataset/NExTVideo/test.csv')
folder_name = f'results_vidagent_{args.model}_vqa_ssparser_multi_question'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for idx, row in tqdm(dataset.iterrows()):
    if idx == 400:
        break
    # test my method
    question = row['question'].capitalize() + '?'
    if question != "Why did the the guy rub his ear after sharing with the group of people?":
        continue
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
    with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','w') as f:
        f.write(f'Question: {question}\n\n')
        f.write(f'Reference Answer: {answer}\n\n')
        f.write(f'Video ID: {row["video"]}\n\n')
        f.write(f'Original program:\n\n```\n{prog}\n```\n')

    init_state = dict(
        QUESTION=question,
        VIDEO=Video.read_file(f'dataset/NExTVideo/videos/{video_id}.mp4'),
        CHOICES=[row['a0'], row['a1'], row['a2'], row['a3'], row['a4']]
    )

    prog = fix(prog, question, module_list, init_state)
    prog += f'\nSELECTED=SELECT(question="{question}",information=ANSWERS0,choices=CHOICES)'
    print(prog)
    with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
        f.write(f'Program:\n\n```\n{prog}\n```\n')
    
    try:
        result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)
        with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
            f.write(f'Rationale:\n\n{html_str}\n\n')
    except Exception as e:
        result = 'Runtime error: ' + str(e)
    print(result)
    with open(f'{folder_name}/{question.replace(" ","_")}_{video_id}.md','a') as f:
        f.write(f'Answer: {result}\n\n')