from engine import visualizer
import os
import sys
import json
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
  sys.path.append(module_path)

from IPython.core.display import HTML
from functools import partial

from engine.utils import ProgramInterpreter
from engine.video import Video

interpreter = ProgramInterpreter()

prog = """TIME=FLAG(begin=None,middle=None,end="at the [end]")
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The boy has turned his head.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)"""

init_state = dict(
    QUESTION = "What does the boy do after turning his head at the end?",
    VIDEO=Video.read_file(f'dataset/NExTVideo/videos/4751951497.mp4'),
    CHOICES = []
)

result, prog_state = interpreter.execute(prog,init_state)

final_text = """VIDQA branch: {'playing the guitar': 5, 'wave at girl': 5, 'take more food': 5, 'look down': 5, 'eat': 5}
VQA branch: {'playing the guitar': 1, 'wave at girl': 5, 'take more food': 1, 'look down': 2, 'eat': 1}
CAP branch: {'playing the guitar': 5, 'wave at girl': 40, 'take more food': 5, 'look down': 30, 'eat': 5}
Answer: wave at girl"""

image = visualizer.visualize(prog, init_state, final_text)

image.save('vis.png')