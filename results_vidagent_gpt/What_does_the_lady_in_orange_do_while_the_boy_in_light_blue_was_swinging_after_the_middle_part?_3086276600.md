Question: What does the lady in orange do while the boy in light blue was swinging after the middle part?

Reference Answer: 3

Video ID: 3086276600

Program:

```
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,question="Is the boy in light blue swinging?",answer="yes")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the lady in orange doing?")
ANSWER0=SELECT(question="What does the lady in orange do while the boy in light blue was swinging after the middle part?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: Invalid clipping times.

