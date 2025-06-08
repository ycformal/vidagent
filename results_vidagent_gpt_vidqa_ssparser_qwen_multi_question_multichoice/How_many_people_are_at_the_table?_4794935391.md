Question: How many people are at the table?

Reference Answer: 0

Video ID: 4794935391

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people are at the table?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people are at the table?")
SELECTED=SELECT(question="How many people are at the table?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many people are at the table?')=<b><span style='color: green;'>User: How many people are at the table?
Assistant: three.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are at the table?, <b><span style='color: darkorange;'>information</span></b>=['User: How many people are at the table?\nAssistant: three.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['three', 'one', 'two', 'seven', 'three'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

