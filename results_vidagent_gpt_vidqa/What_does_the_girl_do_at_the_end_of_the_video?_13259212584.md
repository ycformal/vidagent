Question: What does the girl do at the end of the video?

Reference Answer: 2

Video ID: 13259212584

Program:

```
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP(video=VIDEO,start=ANSWER0-1)
ANSWERS0=VIDQA(video=VIDEO0,question="What is the girl doing?")
ANSWER0=SELECT(question="What does the girl do at the end of the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'frame'

