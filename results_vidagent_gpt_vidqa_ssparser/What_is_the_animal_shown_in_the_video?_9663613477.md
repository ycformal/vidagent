Question: What is the animal shown in the video?

Reference Answer: 1

Video ID: 9663613477

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="What animal is shown in the video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="What animal is shown in the video?")
SELECTED=SELECT(question="What is the animal shown in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='What animal is shown in the video?')=<b><span style='color: green;'>dog</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What is the animal shown in the video?, <b><span style='color: darkorange;'>information</span></b>=['dog'], <b><span style='color: darkorange;'>choices</span></b>=['birds', 'dog', 'squirrel', 'rabbit', 'elephants'])=<b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

