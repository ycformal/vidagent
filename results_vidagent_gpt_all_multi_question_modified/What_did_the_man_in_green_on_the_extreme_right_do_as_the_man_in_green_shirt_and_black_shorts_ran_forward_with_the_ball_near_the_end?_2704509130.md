Question: What did the man in green on the extreme right do as the man in green shirt and black shorts ran forward with the ball near the end?

Reference Answer: 2

Video ID: 2704509130

Original program:

```
TIME=FLAG(begin=None,middle=None,end="near the [end]")
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The man in green shirt and black shorts is running forward with the ball.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in green on the extreme right doing?|What is the man's body position?|Is the man in green on the extreme right interacting with anyone?|What is the man's facial expression?|What is the man's role in the game?|What is the man's position on the field?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end="near the [end]")
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The man in green shirt and black shorts is running forward with the ball.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the man in green on the extreme right doing?|What is the man's body position?|Is the man in green on the extreme right interacting with anyone?|What is the man's facial expression?|What is the man's role in the game?|What is the man's position on the field?")
```

Answer: 4

