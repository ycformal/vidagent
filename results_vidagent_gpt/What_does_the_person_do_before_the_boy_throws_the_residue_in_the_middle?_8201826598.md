Question: What does the person do before the boy throws the residue in the middle?

Reference Answer: 4

Video ID: 8201826598

Program:

```
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,question="Has the boy thrown the residue?",answer="yes")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the person doing?")
ANSWER2=SELECT(question="What does the person do before the boy throws the residue in the middle?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: Invalid clipping times.

