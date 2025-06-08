Question: What does the boy in yellow hold on to as he kisses the baby?

Reference Answer: 1

Video ID: 2889738670

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The boy in yellow is kissing the baby.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the boy in yellow holding on to?|What is the boy's body position?|Is the boy standing or sitting?|What is the boy's facial expression?|Is the boy interacting with anyone else?|What is the context of the boy kissing the baby?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The boy in yellow is kissing the baby.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the boy in yellow holding on to?|What is the boy's body position?|Is the boy standing or sitting?|What is the boy's facial expression?|Is the boy interacting with anyone else?|What is the context of the boy kissing the baby?")
```

Answer: 4

