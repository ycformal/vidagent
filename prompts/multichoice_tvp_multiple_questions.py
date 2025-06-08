import random

GQA_CURATED_EXAMPLES=[
"""Question: How many children are in the video?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many children are there?|How many people appear to be children?|How many kids are present in the scene?|What are the children doing?|Where are the children located?")
""", # DC
"""Question: Why is the blue sweater guy looking at the shirtless men?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="A blue sweater guy is looking at the shirtless men.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Why is the blue sweater guy looking at the shirtless men?|What is the blue sweater guy doing?|What are the shirtless men doing?|What is the blue sweater guy looking at?|Where are the shirtless men in relation to the blue sweater guy?|What is happening around the blue sweater guy and the shirtless men?")
""", #CW
"""Question: Why does the man have to throw the plane first in the middle of the video?
Program:
TIME=FLAG(begin=None,middle="in the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
ANSWERS0=VQA(video=VIDEO0,question="Why does the man have to throw the plane first?|What is the man doing before throwing the plane?|Who is near the man when he throws the plane?|What is the sequence of actions before and after throwing the plane?|How is the man feeling as he prepares to throw the plane?")
""", #CW
"""Question: What does the man in checkered do after walking onto the stage with microphone stands at the start?
Program:
TIME=FLAG(begin="at the [start]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The man in checkered has walked onto the stage with microphone stands.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in checkered doing?|Where does the man in checkered go after entering the stage?|How does the man in checkered interact with the microphone stands?|Who else is on stage with the man in checkered?|How is the man in checkered positioned on stage?")
""", #TN
"""Question: What does the man do after grabbing the boy near the end?
Program:
TIME=FLAG(begin=None,middle=None,end="near the [end]")
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The man has grabbed the boy.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man doing?|What is the boy doing after being grabbed?|How do the man and boy interact after this moment?|How do their (the man and boy) positions change?|What is the mood of the man and boy after this event?")
""", #TN
"""Question: What does the man do after showing the pancake?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man has shown the pancake.")
VIDEO1=CLIP_AFTER(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man doing?|What happens to the pancake after showing the cake?|Does the man interact with anyone after showing the pancake?|What does the man's face look like after showing the pancake?")
""", #TN
"""Question: What does the man playing the drums do with his feet as he plays the drum?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="A man is playing the drum.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man playing the drums doing with his feet?|Is the man using any pedals or foot instruments?|What is the man's posture while playing?|How does the man's body move as he plays the drums?|Are man's feet visible and active?|Describe the movement of the man's feet in detail.")
""", #TC
"""Question: How is the man in grey plaid shirt feeling while talking at the start?
Program:
TIME=FLAG(begin="at the [start]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="A man in grey plaid shirt is talking.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the man in grey plaid shirt feeling?|What facial expressions does the man in grey plaid shirt have?|How is the man in grey plaid shirt's voice or body language?|Who is the man in grey plaid shirt talking to?|What is the context of the man in grey plaid shirt's speech?")
""", #TC
"""Question: How did the boy respond when he saw the girl dancing at the middle of the video?
Program:
TIME=FLAG(begin=None,middle="at the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The boy is seeing the girl dancing.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the boy responding?|What is the boy doing?|What is the boy's facial expression?|Does the boy join in dancing or do something else?|Is the boy talking or gesturing?|What is the girl's response to the boy?")
""", #TC
"""Question: Where is this video taken?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is it?|What is the visible environment or background?|Are there any signs or landmarks?|Is the video indoors or outdoors?|What objects indicate the location?|Describe this scene in detail.")
""", #DL
"""Question: Where did the man in grey rest his hand before he started walking forward?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man in grey has started walking forward.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Where is the man in grey resting his hand?|What is the man in grey doing with his hand?|Is the man in grey's hand on an object or person?|What is the man in grey's hand position relative to his body?|Who or what is near the the man in grey's hand?")
""", #TP
"""Question: What did the baby do before she put the green long toy in her mouth at the middle of the video?
Program:
TIME=FLAG(begin=None,middle="at the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The baby has put the green long toy in her mouth.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the baby doing?|What is the baby's mood or attention?")
""", #TP
"""Question: What did the boy with green car do before he pushed his car the second time?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The boy with green car has pushed his car the second time.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the boy with green car doing?|What is the boy's mood or attention?|Where is the car located before being pushed?|Is the boy talking or interacting with anyone?|What is boy's body position before pushing?|Is the car in motion or stationary?")
""", #TP
"""Question: How did the man ensure that he could see the baby clearly?
Program:
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How is the man ensuring that he can see the baby clearly?|What is the man doing?|What surrounds the man?|How does the man position himself to see the baby?|Does the man move objects or himself for a better view?|Is the baby in the man's direct line of sight?|What actions does the man take to see better?|Are there obstacles between the man and baby?")
""", #DO
"""Question: How did the lady in pink assist the bride in the activity at the beginning?
Program:
TIME=FLAG(begin="at the [beginning]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The lady in pink is assisting the bride in the activity.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the lady in pink assisting the bride in the activity?|What is the lady in pink doing?|What specific action does she perform for the bride?|What is the bride doing at this moment?|Are there tools or objects involved?|What is the interaction between lady in pink and bride?")
""", #CH
"""Question: How did the guy on the board managed to not fall off from the board at the start of the video?
Program:
TIME=FLAG(begin="at the [start] of",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
ANSWERS0=VQA(video=VIDEO0,question="How is the guy on the board managing to not fall off from the board?|How does the guy on the board balance himself?|What is the guy's body position on the board?|Are there supporting objects or people so that guy on the board will not fall?|Is the board stable or moving?|What skills or actions prevent the guy on the board from falling?|Describe the movement of the guy on the board in detail.")
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