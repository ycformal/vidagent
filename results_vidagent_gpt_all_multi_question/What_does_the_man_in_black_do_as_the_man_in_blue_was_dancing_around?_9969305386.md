Question: What does the man in black do as the man in blue was dancing around?

Reference Answer: 4

Video ID: 9969305386

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man in blue is dancing around.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
FRAME1=LOC(video=VIDEO,event="The man in black is doing something.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME1)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in black doing?|How does the man in black react to the man in blue's dancing?|Is the man in black participating in the dancing or doing something else?|What is the man in black's body position?|What is the man in black's facial expression?|Is the man in black interacting with anyone else?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man in blue is dancing around.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
FRAME1=LOC(video=VIDEO,event="The man in black is doing something.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME1)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in black doing?|How does the man in black react to the man in blue's dancing?|Is the man in black participating in the dancing or doing something else?|What is the man in black's body position?|What is the man in black's facial expression?|Is the man in black interacting with anyone else?")
```

Answer: 4

