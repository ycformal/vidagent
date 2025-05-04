Question: What did the child do before opening the door at the middle?

Reference Answer: 0

Video ID: 12884491894

Program:

```
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,question="Has the child opened the door?",answer="yes")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the child doing?")
ANSWER0=SELECT(question="What did the child do before opening the door at the middle?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: Invalid clipping times.

