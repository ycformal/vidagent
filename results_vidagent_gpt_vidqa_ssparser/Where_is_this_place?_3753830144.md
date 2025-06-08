Question: Where is this place?

Reference Answer: 0

Video ID: 3753830144

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this place?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this place?")
SELECTED=SELECT(question="Where is this place?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this place?')=<b><span style='color: green;'>classroom</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this place?, <b><span style='color: darkorange;'>information</span></b>=['classroom'], <b><span style='color: darkorange;'>choices</span></b>=['classroom', 'porch outside house', 'train station', 'bus terminal', 'mountain'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

