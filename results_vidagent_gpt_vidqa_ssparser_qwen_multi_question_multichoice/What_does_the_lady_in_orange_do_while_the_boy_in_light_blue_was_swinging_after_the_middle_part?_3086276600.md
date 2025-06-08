Question: What does the lady in orange do while the boy in light blue was swinging after the middle part?

Reference Answer: 3

Video ID: 3086276600

Original program:

```
TIME=FLAG(begin=None,middle="after the [middle] part",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The boy in light blue is swinging.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
FRAME1=LOC(video=VIDEO1,event="The lady in orange is doing something.")
VIDEO2=CLIP_AFTER(video=VIDEO1,frame=FRAME1)
ANSWERS0=VQA(video=VIDEO2,question="What is the lady in orange doing?|How is the lady in orange feeling?|What surrounds the lady in orange?|What is the boy in light blue doing?|How is the boy in light blue feeling?|What surrounds the boy in light blue?")
```
Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="What does the lady in orange do while the boy in light blue was swinging after the middle part?")
SELECTED=SELECT(question="What does the lady in orange do while the boy in light blue was swinging after the middle part?",information=ANSWERS0,choices=CHOICES)
```
Answer: Runtime error: 'begin'

