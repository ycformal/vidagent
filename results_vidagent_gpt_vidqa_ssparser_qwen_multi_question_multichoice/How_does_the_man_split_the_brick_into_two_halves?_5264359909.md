Question: How does the man split the brick into two halves?

Reference Answer: 0

Video ID: 5264359909

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How does the man split the brick into two halves?|What is the man doing?|What surrounds the man?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How does the man split the brick into two halves?|What is the man doing?|What surrounds the man?")
SELECTED=SELECT(question="How does the man split the brick into two halves?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How does the man split the brick into two halves?|What is the man doing?|What surrounds the man?')=<b><span style='color: green;'>User: How does the man split the brick into two halves?
Assistant: use mallet to hit

User: What is the man doing?
Assistant: The man is demonstrating or explaining something related to the stone blocks.

User: What surrounds the man?
Assistant: The man is surrounded by a group of people, some of whom are taking photos or videos with their cameras.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How does the man split the brick into two halves?, <b><span style='color: darkorange;'>information</span></b>=['User: How does the man split the brick into two halves?\nAssistant: use mallet to hit\n\nUser: What is the man doing?\nAssistant: The man is demonstrating or explaining something related to the stone blocks.\n\nUser: What surrounds the man?\nAssistant: The man is surrounded by a group of people, some of whom are taking photos or videos with their cameras.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['use mallet to hit', 'use a diamond cutter', 'with a axe', 'throw from high building', 'throw another brick on brick'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

