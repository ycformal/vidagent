Question: What does the guy in red do after pointing at the shark at the start?

Reference Answer: 2

Video ID: 2669597217

Original program:

```
TIME=FLAG(begin="at the [start]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The guy in red is pointing at the shark.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the guy in red doing?|What is the guy's facial expression?|What is the guy's body language?|What is the guy's position in relation to the shark?|Does the guy interact with anyone after pointing at the shark?|What is the mood of the guy after pointing at the shark?")
```

Program:

```
TIME=FLAG(begin="at the [start]",middle=None,end=None)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,event="The guy in red is pointing at the shark.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the guy in red doing?|What is the guy's facial expression?|What is the guy's body language?|What is the guy's position in relation to the shark?|Does the guy interact with anyone after pointing at the shark?|What is the mood of the guy after pointing at the shark?")
```

Answer: 3

