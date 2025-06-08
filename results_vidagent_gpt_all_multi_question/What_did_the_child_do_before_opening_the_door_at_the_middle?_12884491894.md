Question: What did the child do before opening the door at the middle?

Reference Answer: 0

Video ID: 12884491894

Original program:

```
TIME=FLAG(begin=None,middle="at the [middle]",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The child has opened the door.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the child doing?|What is the child's mood or attention?|What is the child's body position before opening the door?|Is the child interacting with anyone or anything?|What is the child's facial expression before opening the door?|What is the child's hand position before opening the door?")
```

Program:

```
TIME=FLAG(begin=None,middle="at the [middle]",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The child has opened the door.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the child doing?|What is the child's mood or attention?|What is the child's body position before opening the door?|Is the child interacting with anyone or anything?|What is the child's facial expression before opening the door?|What is the child's hand position before opening the door?")
```

Answer: 2

