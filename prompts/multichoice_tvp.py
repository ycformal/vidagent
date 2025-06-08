import random

GQA_CURATED_EXAMPLES=[
"""Question: How many children are in the video?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many children are there?")
""", # DC
"""Question: Why is the blue sweater guy looking at the shirtless men?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="A blue sweater guy is looking at the shirtless men.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Why is the blue sweater guy looking at the shirtless men?")
""", #CW
"""Question: Why does the man have to throw the plane first in the middle of the video?
Program:
TIME=FLAG(begin=None,middle="in the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
ANSWERS0=VQA(video=VIDEO0,question="Why does the man have to throw the plane first?")
""", #CW
"""Question: What does the man in checkered do after walking onto the stage with microphone stands at the start?
Program:
TIME=FLAG(begin="at the [start]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The man in checkered has walked onto the stage with microphone stands.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in checkered doing?")
""", #TN
"""Question: What does the man do after grabbing the boy near the end?
Program:
TIME=FLAG(begin=None,middle=None,end="near the [end]")
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The man has grabbed the boy.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man doing?")
""", #TN
"""Question: What does the man do after showing the pancake?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man has shown the pancake.")
VIDEO1=CLIP_AFTER(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man doing?")
""", #TN
"""Question: What does the man playing the drums do with his feet as he plays the drum?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="A man is playing the drum.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man playing the drums doing with his feet?")
""", #TC
"""Question: How is the man in grey plaid shirt feeling while talking at the start?
Program:
TIME=FLAG(begin="at the [start]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="A man in grey plaid shirt is talking.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the man in grey plaid shirt feeling?")
""", #TC
"""Question: How did the boy respond when he saw the girl dancing at the middle of the video?
Program:
TIME=FLAG(begin=None,middle="at the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The boy is seeing the girl dancing.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the boy responding?")
""", #TC
"""Question: Where is this video taken?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is it?")
""", #DL
"""Question: Where did the man in grey rest his hand before he started walking forward?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man in grey has started walking forward.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Where is the man in grey resting his hand?")
""", #TP
"""Question: What did the baby do before she put the green long toy in her mouth at the middle of the video?
Program:
TIME=FLAG(begin=None,middle="at the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The baby has put the green long toy in her mouth.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the baby doing?")
""", #TP
"""Question: What did the boy with green car do before he pushed his car the second time?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The boy with green car has pushed his car the second time.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the boy with green car doing?")
""", #TP
"""Question: How did the man ensure that he could see the baby clearly?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How is the man ensuring that he can see the baby clearly?")
""", #DO
"""Question: How did the lady in pink assist the bride in the activity at the beginning?
Program:
TIME=FLAG(begin="at the [beginning]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The lady in pink is assisting the bride in the activity.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the lady in pink assisting the bride in the activity?")
""", #CH
"""Question: How did the guy on the board managed to not fall off from the board at the start of the video?
Program:
TIME=FLAG(begin="at the [start] of",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
ANSWERS0=VQA(video=VIDEO0,question="How is the guy on the board managing to not fall off from the board?")
""" #DO
]

def create_prompt(inputs,num_prompts=8,method='random',seed=42,group=0):
    if method=='all':
        prompt_examples = GQA_CURATED_EXAMPLES
    elif method=='random':
        random.seed(seed)
        prompt_examples = random.sample(GQA_CURATED_EXAMPLES,num_prompts)
    else:
        raise NotImplementedError

    prompt_examples = '\n'.join(prompt_examples)
    prompt_examples = f'Think step by step to answer the question.\n\n{prompt_examples}'


    return prompt_examples + "\nQuestion: {question}\nProgram:\n".format(**inputs)