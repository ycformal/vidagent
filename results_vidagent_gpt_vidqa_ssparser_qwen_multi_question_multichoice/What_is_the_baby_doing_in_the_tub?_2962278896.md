Question: What is the baby doing in the tub?

Reference Answer: 4

Video ID: 2962278896

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="What is the baby doing in the tub?|How is the baby feeling?|What surrounds the baby?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="What is the baby doing in the tub?|How is the baby feeling?|What surrounds the baby?")
SELECTED=SELECT(question="What is the baby doing in the tub?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='What is the baby doing in the tub?|How is the baby feeling?|What surrounds the baby?')=<b><span style='color: green;'>User: What is the baby doing in the tub?
Assistant: playing with toy duck

User: How is the baby feeling?
Assistant: The baby appears to be in a state of rest or sleep.

User: What surrounds the baby?
Assistant: The baby is surrounded by a patterned fabric, possibly a blanket or a piece of clothing.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What is the baby doing in the tub?, <b><span style='color: darkorange;'>information</span></b>=['User: What is the baby doing in the tub?\nAssistant: playing with toy duck\n\nUser: How is the baby feeling?\nAssistant: The baby appears to be in a state of rest or sleep.\n\nUser: What surrounds the baby?\nAssistant: The baby is surrounded by a patterned fabric, possibly a blanket or a piece of clothing.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['playing with water balloons', 'playing with toy duck', 'swimming', 'taking a video', 'showering'])=<b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

