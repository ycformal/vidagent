Question: How many dogs are there in the video?

Reference Answer: 0

Video ID: 8064396272

Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="How many dogs are there?")
ANSWER0=SELECT(question="How many dogs are there in the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many dogs are there?')=<b><span style='color: green;'>three</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many dogs are there in the video?, <b><span style='color: darkorange;'>information</span></b>=['three'], <b><span style='color: darkorange;'>choices</span></b>=['three', 'two', 'five', 'four', 'one'])=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

