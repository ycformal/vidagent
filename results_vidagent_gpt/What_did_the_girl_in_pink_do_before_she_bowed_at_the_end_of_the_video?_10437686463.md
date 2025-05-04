Question: What did the girl in pink do before she bowed at the end of the video?

Reference Answer: 1

Video ID: 10437686463

Program:

```
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,question="Has the girl in pink bowed?",answer="yes")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the girl in pink doing?")
ANSWER1=SELECT(question="What did the girl in pink do before she bowed at the end of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: Invalid clipping times.

