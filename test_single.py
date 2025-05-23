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

prog = """FRAME0=LOC(video=VIDEO,event="The first man has stopped.")
VIDEO1=CLIP_AFTER(video=VIDEO,frame=FRAME0)
ANSWERS0=VIDQA(video=VIDEO1,question="What is the first man doing?")
ANSWER0=SELECT(question="What does the first man do after stopping?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)"""
# prog = """ANSWERS0=VIDQA(video=VIDEO,question="How did the lady position her legs as she was going down?")
# ANSWER0=SELECT(question="How did the lady position her legs as she was going down?",information=ANSWERS0,choices=CHOICES)
# FINAL_RESULT=RESULT(var=ANSWER0)"""
question = "What does the first man do after stopping?"

init_state = dict(
    VIDEO=Video.read_file(f'dataset/NExTVideo/videos/2732002300.mp4'),
    CHOICES=['move to the side', 'grab the back of his chair', 'swing the dog', 'wave', 'smoke']
)

result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)

print(prog_state)

for key, value in init_state.items():
    if isinstance(value, Video):
        value.save(key + '.mp4')