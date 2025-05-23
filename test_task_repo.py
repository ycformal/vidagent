import os
os.environ["HF_HOME"] = "/home/hice1/yxu846/scratch/models"
import sys
import json
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
  sys.path.append(module_path)

from IPython.core.display import HTML
from functools import partial

from engine.utils import ProgramGenerator
from prompts.multichoice_vidqa import create_prompt
from engine.ssparser import fix
from engine.video import Video

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
import openai
key = "tl.qspk.W5DyWbibnie1gou72KsNFzm2xtUltPk3bLuROweJsThTbc[IfLY:nogngujZVN{[ljus5rjxdLU4CmclGK{BHtxj`vvD6PLQiyZ1121yskCtUEk9bjQXX3.B1`25:4NQ[fuNnJGBdwMQHK[Tewgt:e4h.SNB"
key = ''.join([chr(ord(k)-1) for k in key])
openai.api_key=key

module_list = [
    "LOC", "CLIP", "CLIP_BEFORE", "CLIP_AFTER", "CLIP_AROUND", "EVAL",
    "LENGTH", "VQA", "VIDQA", "CAP", "RESULT", 'SELECT'
]
init_state = dict(
    VIDEO=Video.read_file(f'dataset/NExTVideo/videos/7492345390.mp4'),
    CHOICES=['cross one leg over the other', 'touch baby s foot', 'playing with sofa', 'dance', 'cross her arms']
)
question = "How did the baby react after the man touched its head at the end of the video?"
prog,_ = generator.generate(dict(question=question))
print(prog)
prog = fix(prog, question, module_list, init_state)
print(prog)