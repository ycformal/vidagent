Question: What is the relationship between the people on stage?

Reference Answer: 4

Video ID: 3571539122

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="What is the relationship between the people on stage?|How do the people on stage know each other?|What is the dynamic between the people on stage?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="What is the relationship between the people on stage?|How do the people on stage know each other?|What is the dynamic between the people on stage?")
SELECTED=SELECT(question="What is the relationship between the people on stage?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='What is the relationship between the people on stage?|How do the people on stage know each other?|What is the dynamic between the people on stage?')=<b><span style='color: green;'>User: What is the relationship between the people on stage?
Assistant: team member

User: How do the people on stage know each other?
Assistant: The people on stage appear to be familiar with each other, as they are performing a synchronized dance routine together.

User: What is the dynamic between the people on stage?
Assistant: The dynamic between the people on stage is one of coordination and teamwork, as they perform synchronized dance moves.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What is the relationship between the people on stage?, <b><span style='color: darkorange;'>information</span></b>=['User: What is the relationship between the people on stage?\nAssistant: team member\n\nUser: How do the people on stage know each other?\nAssistant: The people on stage appear to be familiar with each other, as they are performing a synchronized dance routine together.\n\nUser: What is the dynamic between the people on stage?\nAssistant: The dynamic between the people on stage is one of coordination and teamwork, as they perform synchronized dance moves.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['coworkers', 'team member', 'rock', 'work mates', 'friends'])=<b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

