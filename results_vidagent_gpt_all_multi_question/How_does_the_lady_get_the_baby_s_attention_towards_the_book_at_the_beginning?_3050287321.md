Question: How does the lady get the baby s attention towards the book at the beginning?

Reference Answer: 1

Video ID: 3050287321

Original program:

```
TIME=FLAG(begin="at the [beginning]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The lady is getting the baby's attention towards the book.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How does the lady get the baby's attention towards the book?|What is the lady doing?|What is the baby's initial focus?|What is the lady's body position in relation to the baby?|Does the lady use any objects or gestures to get the baby's attention?|What is the baby's reaction to the lady's actions?")
```

Program:

```
TIME=FLAG(begin="at the [beginning]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The lady is getting the baby's attention towards the book.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How does the lady get the baby's attention towards the book?|What is the lady doing?|What is the baby's initial focus?|What is the lady's body position in relation to the baby?|Does the lady use any objects or gestures to get the baby's attention?|What is the baby's reaction to the lady's actions?")
```

Answer: 2

