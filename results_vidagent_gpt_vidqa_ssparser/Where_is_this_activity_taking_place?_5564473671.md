Question: Where is this activity taking place?

Reference Answer: 2

Video ID: 5564473671

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this activity taking place?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this activity taking place?")
SELECTED=SELECT(question="Where is this activity taking place?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this activity taking place?')=<b><span style='color: green;'>archery practice</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this activity taking place?, <b><span style='color: darkorange;'>information</span></b>=['archery practice'], <b><span style='color: darkorange;'>choices</span></b>=['house', 'petting zoo', 'archery practice', 'carpark', 'museum'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

