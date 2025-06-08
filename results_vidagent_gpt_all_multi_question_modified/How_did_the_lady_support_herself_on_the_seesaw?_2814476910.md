Question: How did the lady support herself on the seesaw?

Reference Answer: 1

Video ID: 2814476910

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The lady is supporting herself on the seesaw.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="How is the lady supporting herself on the seesaw?|What is the lady's body position on the seesaw?|What is the lady's facial expression?|Is the lady using any objects or people for support?|What is the lady's posture on the seesaw?|Is the seesaw in motion or stationary?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The lady is supporting herself on the seesaw.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="How is the lady supporting herself on the seesaw?|What is the lady's body position on the seesaw?|What is the lady's facial expression?|Is the lady using any objects or people for support?|What is the lady's posture on the seesaw?|Is the seesaw in motion or stationary?")
```

Answer: 4

