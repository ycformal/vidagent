Question: What did the lady in green do after the other lady glide backwards?

Reference Answer: 2

Video ID: 6068969659

Program:

```
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,question="Has the other lady glided backwards?",answer="yes")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the lady in green doing?")
ANSWER1=SELECT(question="What did the lady in green do after the other lady glide backwards?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: Invalid clipping times.

