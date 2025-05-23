Question: What does the baby do to his hands at the end?

Reference Answer: 2

Video ID: 7486609038

Program:

```
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP(video=VIDEO,frame=ANSWER0)
ANSWERS0=VIDQA(video=VIDEO0,question="What is the baby doing to his hands?")
ANSWER0=SELECT(question="What does the baby do to his hands at the end?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: object of type 'float' has no len()

