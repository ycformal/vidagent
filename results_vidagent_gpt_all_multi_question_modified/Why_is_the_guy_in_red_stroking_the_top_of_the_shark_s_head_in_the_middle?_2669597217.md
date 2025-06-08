Question: Why is the guy in red stroking the top of the shark s head in the middle?

Reference Answer: 0

Video ID: 2669597217

Original program:

```
TIME=FLAG(begin=None,middle="in the [middle]",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The guy in red is stroking the top of the shark's head.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="Why is the guy in red stroking the top of the shark's head?|What is the guy in red doing?|What is the shark's reaction to the guy's action?|Is the guy in red interacting with anyone else?|What is the mood of the guy in red while stroking the shark's head?|What is the location of the guy in red in relation to the shark?")
```

Program:

```
TIME=FLAG(begin=None,middle="in the [middle]",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The guy in red is stroking the top of the shark's head.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="Why is the guy in red stroking the top of the shark's head?|What is the guy in red doing?|What is the shark's reaction to the guy's action?|Is the guy in red interacting with anyone else?|What is the mood of the guy in red while stroking the shark's head?|What is the location of the guy in red in relation to the shark?")
```

Answer: 4

