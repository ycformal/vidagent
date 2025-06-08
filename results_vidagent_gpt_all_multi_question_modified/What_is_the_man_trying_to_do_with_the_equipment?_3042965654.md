Question: What is the man trying to do with the equipment?

Reference Answer: 2

Video ID: 3042965654

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man is trying to use the equipment.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man trying to do with the equipment?|What is the man's goal or intention?|What is the man's body position in relation to the equipment?|Is the man successful in using the equipment?|What is the man's facial expression while using the equipment?|What is the man's level of focus or concentration?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man is trying to use the equipment.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man trying to do with the equipment?|What is the man's goal or intention?|What is the man's body position in relation to the equipment?|Is the man successful in using the equipment?|What is the man's facial expression while using the equipment?|What is the man's level of focus or concentration?")
```

Answer: 2

