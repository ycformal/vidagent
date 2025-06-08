Question: What did the boy do when he first turned to his left after the middle part?

Reference Answer: 2

Video ID: 5031528157

Original program:

```
TIME=FLAG(begin=None,middle="after the [middle] part",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The boy has turned to his left.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What did the boy do when he first turned to his left?|What is the boy doing?|What surrounds the boy?|How is the boy feeling?")
```
Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="What did the boy do when he first turned to his left after the middle part?")
SELECTED=SELECT(question="What did the boy do when he first turned to his left after the middle part?",information=ANSWERS0,choices=CHOICES)
```
Answer: Runtime error: 'begin'

