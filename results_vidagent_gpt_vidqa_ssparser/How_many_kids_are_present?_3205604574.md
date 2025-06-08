Question: How many kids are present?

Reference Answer: 1

Video ID: 3205604574

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many kids are present?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many kids are present?")
SELECTED=SELECT(question="How many kids are present?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many kids are present?')=<b><span style='color: green;'>two</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many kids are present?, <b><span style='color: darkorange;'>information</span></b>=['two'], <b><span style='color: darkorange;'>choices</span></b>=['six', 'two', 'three', 'one', 'nine'])=<b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

