Question: How did the man in white guide the crane operator?

Reference Answer: 3

Video ID: 2757193865

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man in white is guiding the crane operator.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="How is the man in white guiding the crane operator?|What specific actions is the man in white taking?|What is the crane operator doing?|What is the man in white's body position relative to the crane operator?|Is the man in white using any tools or equipment?|What is the communication between the man in white and the crane operator?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man in white is guiding the crane operator.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="How is the man in white guiding the crane operator?|What specific actions is the man in white taking?|What is the crane operator doing?|What is the man in white's body position relative to the crane operator?|Is the man in white using any tools or equipment?|What is the communication between the man in white and the crane operator?")
```

Answer: 3

