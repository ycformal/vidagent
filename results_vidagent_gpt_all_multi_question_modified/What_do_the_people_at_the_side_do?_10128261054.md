Question: What do the people at the side do?

Reference Answer: 3

Video ID: 10128261054

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="People are at the side.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What are the people at the side doing?|What is their body position?|Are they interacting with anyone?|What is the context of their actions?|Do they have any objects or tools with them?|Describe the people at the side in detail.")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="People are at the side.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What are the people at the side doing?|What is their body position?|Are they interacting with anyone?|What is the context of their actions?|Do they have any objects or tools with them?|Describe the people at the side in detail.")
```

Answer: 3

