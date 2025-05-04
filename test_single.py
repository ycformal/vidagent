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

prog = """ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The man in black has pushed the equipment up.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in darkgreen doing?")
ANSWER2=SELECT(question="What does the man in darkgreen do after the man in black pushed the equipment up in the middle of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER2)"""
question = "What does the man in darkgreen do after the man in black pushed the equipment up in the middle fo the video?"

init_state = dict(
    VIDEO=Video.read_file(f'dataset/NExTVideo/videos/3042965654.mp4'),
    CHOICES=['hold the lady s hand','drink from it','look at the man','point to him and smile','walk over']
)

result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)

for key, value in init_state.items():
    if isinstance(value, Video):
        value.save(key + '.mp4')

print(prog_state)