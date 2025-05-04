import random

GQA_CURATED_EXAMPLES=[
"""Question: How many children are in the video?
Program:
ANSWERS0=VQA(video=VIDEO,question="How many children are there?")
ANSWER0=SELECT(question="How many children are in the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Why is the blue sweater guy looking at the shirtless men?
Program:
FRAME0=LOC(video=VIDEO,question="Is the blue sweater guy looking at the shirtless men?",answer="yes")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Why is the blue sweater guy looking at the shirtless men?")
ANSWER0=SELECT(question="Why is the blue sweater guy looking at the shirtless men?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: How did the guy on the board managed to not fall off from the board at the start of the video?
Program:
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
ANSWERS0=VQA(video=VIDEO0,question="How is the guy on the board managing to not fall off from the board?")
ANSWER0=SELECT(question="How did the guy on the board managed to not fall off from the board at the start of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Why does the man have to throw the plane first in the middle of the video?
Program:
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
ANSWERS0=VQA(video=VIDEO0,question="Why does the man have to throw the plane first?")
ANSWER2=SELECT(question="Why does the man have to throw the plane first in the middle of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: What does the man in checkered do after walking onto the stage with microphone stands at the start?
Program:
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,question="Has the man in checkered walked onto the stage with microphone stands?",answer="yes")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man in checkered doing?")
ANSWER0=SELECT(question="What does the man in checkered do after walking onto the stage with microphone stands at the start?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: What does the man playing the drums do with his feet as he plays the drum?
Program:
FRAME0=LOC(video=VIDEO,question="Is the man playing the drums?",answer="yes")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man playing the drums doing with his feet?")
ANSWER0=SELECT(question="What does the man playing the drums do with his feet as he plays the drum?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: How is the man in grey plaid shirt feeling while talking at the start?
Program:
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="Is the man in gray plaid shirt talking?")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the man in grey plaid shirt feeling?")
ANSWER0=SELECT(question="How is the man in grey plaid shirt feeling while talking at the start?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Where is this video taken?
Program:
ANSWERS0=VQA(video=VIDEO,question="Where is it?")
ANSWER0=SELECT(question="Where is this video taken?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Where did the man in grey rest his hand before he started walking forward?
Program:
FRAME0=LOC(video=VIDEO,question="Has the man in grey started walking forward?",answer="yes")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Where is the man in grey resting his hand?")
ANSWER0=SELECT(question="Where did the man in grey rest his hand before he started walking forward?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: How did the man ensure that he could see the baby clearly?
Program:
ANSWERS0=VQA(video=VIDEO,question="How is the man ensuring that he can see the baby clearly?")
ANSWER0=SELECT(question="How did the man ensure that he could see the baby clearly?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: How did the lady in pink assist the bride in the activity at the beginning?
Program:
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
ANSWERS0=VQA(video=VIDEO0,question="How is the lady in pink assisting the bride in the activity?")
ANSWER0=SELECT(question="How did the lady in pink assist the bride in the activity at the beginning?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: What does the man do after grabbing the boy near the end?
Program:
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,question="Has the man grabbed the boy?",answer="yes")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man doing?")
ANSWER1=SELECT(question="What does the man do after grabbing the boy near the end?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER1)
"""
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