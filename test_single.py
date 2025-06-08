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

prompter = partial(create_prompt,method='all')
generator = ProgramGenerator(prompter=prompter, model_name_or_path=model)
interpreter = ProgramInterpreter()
import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key

prog = """FRAME0=LOC(video=VIDEO,event="Two men on the left are playing instruments.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VLM(video=VIDEO0,question="How are the two men on the left playing their instruments?")"""
# prog = """ANSWERS0=VIDQA(video=VIDEO,question="How did the lady position her legs as she was going down?")
# ANSWER0=SELECT(question="How did the lady position her legs as she was going down?",information=ANSWERS0,choices=CHOICES)
# FINAL_RESULT=RESULT(var=ANSWER0)"""
question = "How do the two men on the left play their instruments?"

init_state = dict(
    VIDEO=Video.read_file(f'dataset/NExTVideo/videos/2906873825.mp4'),
    CHOICES=['blow', 'tap feet', 'strum the string', 'press the keys', 'hit with sticks']
)

result, prog_state = interpreter.execute(prog,init_state)

print(result)
print(prog_state)

for key, value in init_state.items():
    if isinstance(value, Video):
        value.save(key + '.mp4')