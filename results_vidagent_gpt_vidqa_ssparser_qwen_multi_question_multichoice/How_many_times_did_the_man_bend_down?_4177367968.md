Question: How many times did the man bend down?

Reference Answer: 1

Video ID: 4177367968

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWER0=COUNT(video=VIDEO,action="bend down")
ANSWERS0=VQA(video=VIDEO,question="How many times did the man bend down?|What is the man doing?|What surrounds the man?")
```
Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="How many times did the man bend down?")
SELECTED=SELECT(question="How many times did the man bend down?",information=ANSWERS0,choices=CHOICES)
```
Answer: Runtime error: 'begin'

