Question: What was the man in white shirt doing as the man in green passed by him?

Reference Answer: 3

Video ID: 6813372954

Program:

```
FRAME0=LOC(video=VIDEO,event="The man in white shirt is standing.")
FRAME1=LOC(video=VIDEO,event="The man in green is passing by the man in white shirt.")
VIDEO0=CLIP_BETWEEN(video=VIDEO,start_frame=FRAME0,end_frame=FRAME1)
ANSWERS0=VQA(video=VIDEO0,question="What is the man in white shirt doing?")
ANSWER0=SELECT(question="What was the man in white shirt doing as the man in green passed by him?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CLIP_BETWEEN'

