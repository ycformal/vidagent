Question: Where is the video taken?

Reference Answer: 2

Video ID: 5622582668

Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="Where is the video taken?")
ANSWER0=SELECT(question="Where is the video taken?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: Expecting ',' delimiter: line 2 column 290 (char 291)

