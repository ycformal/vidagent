Question: Where are the people hanging out?

Reference Answer: 0

Video ID: 3747890905

Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="Where are the people hanging out?")
ANSWER0=SELECT(question="Where are the people hanging out?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where are the people hanging out?')=<b><span style='color: green;'>living room</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where are the people hanging out?, <b><span style='color: darkorange;'>information</span></b>=['living room'], <b><span style='color: darkorange;'>choices</span></b>=['living room', 'play area', 'jungle', 'by the thams', 'studio'])=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

