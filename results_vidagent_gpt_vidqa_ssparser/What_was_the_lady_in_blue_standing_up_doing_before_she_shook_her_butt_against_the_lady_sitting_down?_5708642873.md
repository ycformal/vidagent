Question: What was the lady in blue standing up doing before she shook her butt against the lady sitting down?

Reference Answer: 2

Video ID: 5708642873

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The lady in blue is standing up.")
FRAME1=LOC(video=VIDEO,event="The lady in blue is shaking her butt against the lady sitting down.")
VIDEO0=CLIP_BETWEEN(video=VIDEO,start_frame=FRAME0,end_frame=FRAME1)
ANSWERS0=VQA(video=VIDEO0,question="What was the lady in blue doing before she shook her butt against the lady sitting down?")
```
Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="What was the lady in blue standing up doing before she shook her butt against the lady sitting down?")
SELECTED=SELECT(question="What was the lady in blue standing up doing before she shook her butt against the lady sitting down?",information=ANSWERS0,choices=CHOICES)
```
Answer: Runtime error: 'begin'

