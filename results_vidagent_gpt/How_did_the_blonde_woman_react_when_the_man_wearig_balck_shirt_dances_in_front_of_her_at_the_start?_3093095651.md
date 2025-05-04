Question: How did the blonde woman react when the man wearig balck shirt dances in front of her at the start?

Reference Answer: 3

Video ID: 3093095651

Program:

```
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=0)
FRAME0=LOC(video=VIDEO0,question="Is the man wearing black shirt dancing in front of the blonde woman?",answer="yes")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="How is the blonde woman reacting?")
ANSWER0=SELECT(question="How did the blonde woman react when the man wearing black shirt dances in front of her at the start?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: Invalid clipping times.

