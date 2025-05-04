Question: What was the leopard doing before it jumped up the last time near the end?

Reference Answer: 1

Video ID: 3360428599

Program:

```
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,question="Has the leopard jumped up?",answer="yes")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What was the leopard doing?")
ANSWER1=SELECT(question="What was the leopard doing before it jumped up the last time near the end?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: Invalid clipping times.

