Question: What did the small elephant do at the end?

Reference Answer: 4

Video ID: 6862984319

Program:

```
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP(video=VIDEO,frame=ANSWER0)
ANSWERS0=VIDQA(video=VIDEO0,question="What is the small elephant doing?")
ANSWER0=SELECT(question="What did the small elephant do at the end?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: object of type 'float' has no len()

