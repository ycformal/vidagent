Question: Where is this happening?

Reference Answer: 2

Video ID: 4536434821

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this happening?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this happening?")
SELECTED=SELECT(question="Where is this happening?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this happening?')=<b><span style='color: green;'>garden</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this happening?, <b><span style='color: darkorange;'>information</span></b>=['garden'], <b><span style='color: darkorange;'>choices</span></b>=['on the road', 'room', 'garden', 'bus', 'bedroom'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

