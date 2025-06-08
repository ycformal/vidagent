Question: How is the man feeding the baby?

Reference Answer: 4

Video ID: 5073490515

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How is the man feeding the baby?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How is the man feeding the baby?")
SELECTED=SELECT(question="How is the man feeding the baby?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How is the man feeding the baby?')=<b><span style='color: green;'>spoon.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How is the man feeding the baby?, <b><span style='color: darkorange;'>information</span></b>=['spoon.'], <b><span style='color: darkorange;'>choices</span></b>=['hand', 'bowl', 'cup', 'chopsticks', 'spoon'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

