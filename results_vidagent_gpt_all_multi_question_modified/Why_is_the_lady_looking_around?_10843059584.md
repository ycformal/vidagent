Question: Why is the lady looking around?

Reference Answer: 0

Video ID: 10843059584

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The lady is looking around.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Why is the lady looking around?|What is the lady's facial expression?|What is the lady's body language?|What is the context of the lady looking around?|Is the lady searching for something or someone?|What is the lady's gaze focused on?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The lady is looking around.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Why is the lady looking around?|What is the lady's facial expression?|What is the lady's body language?|What is the context of the lady looking around?|Is the lady searching for something or someone?|What is the lady's gaze focused on?")
```

Answer: 0

