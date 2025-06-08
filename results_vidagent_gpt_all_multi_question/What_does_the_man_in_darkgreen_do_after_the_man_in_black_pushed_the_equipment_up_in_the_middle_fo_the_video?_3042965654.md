Question: What does the man in darkgreen do after the man in black pushed the equipment up in the middle fo the video?

Reference Answer: 2

Video ID: 3042965654

Original program:

```
TIME=FLAG(begin=None,middle="in the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The man in black has pushed the equipment up.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in darkgreen doing?|What is the man in darkgreen's reaction to the man in black pushing the equipment?|Does the man in darkgreen interact with the equipment or the man in black?|What is the man in darkgreen's body position?|What is the mood of the man in darkgreen after the event?")
```

Program:

```
TIME=FLAG(begin=None,middle="in the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The man in black has pushed the equipment up.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in darkgreen doing?|What is the man in darkgreen's reaction to the man in black pushing the equipment?|Does the man in darkgreen interact with the equipment or the man in black?|What is the man in darkgreen's body position?|What is the mood of the man in darkgreen after the event?")
```

Answer: 3

