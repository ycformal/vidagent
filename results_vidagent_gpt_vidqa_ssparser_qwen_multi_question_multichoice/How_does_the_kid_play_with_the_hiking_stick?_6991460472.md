Question: How does the kid play with the hiking stick?

Reference Answer: 2

Video ID: 6991460472

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How does the kid play with the hiking stick?|What is the kid doing?|What surrounds the kid?|How is the kid feeling?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How does the kid play with the hiking stick?|What is the kid doing?|What surrounds the kid?|How is the kid feeling?")
SELECTED=SELECT(question="How does the kid play with the hiking stick?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How does the kid play with the hiking stick?|What is the kid doing?|What surrounds the kid?|How is the kid feeling?')=<b><span style='color: green;'>User: How does the kid play with the hiking stick?
Assistant: pokes the ground

User: What is the kid doing?
Assistant: The kid is holding a stick and walking alongside the woman.

User: What surrounds the kid?
Assistant: The kid is surrounded by dry bushes and a clear sky.

User: How is the kid feeling?
Assistant: The kid appears to be excited and happy.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How does the kid play with the hiking stick?, <b><span style='color: darkorange;'>information</span></b>=['User: How does the kid play with the hiking stick?\nAssistant: pokes the ground\n\nUser: What is the kid doing?\nAssistant: The kid is holding a stick and walking alongside the woman.\n\nUser: What surrounds the kid?\nAssistant: The kid is surrounded by dry bushes and a clear sky.\n\nUser: How is the kid feeling?\nAssistant: The kid appears to be excited and happy.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['pulling it', 'hold her hand', 'pokes the ground', 'sled', 'with both hands'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

