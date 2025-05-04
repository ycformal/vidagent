Question: How did the car move while crossing the river?

Reference Answer: 4

Video ID: 5929534589

Program:

```
ANSWERS0=VQA(video=VIDEO,question="How is the car moving while crossing the river?")
ANSWER0=SELECT(question="How did the car move while crossing the river?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How is the car moving while crossing the river?')=<b><span style='color: green;'>['driving', 'driving', 'truck', 'driving', 'driving', 'driving', 'driving', 'driving', 'driving', 'no', 'no car']</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How did the car move while crossing the river?, <b><span style='color: darkorange;'>information</span></b>=['driving', 'driving', 'truck', 'driving', 'driving', 'driving', 'driving', 'driving', 'driving', 'no', 'no car'], <b><span style='color: darkorange;'>choices</span></b>=['quickly', 'did not move', 'speedily', 'hurriedly', 'slowly'])=<b><span style='color: green;'>4</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

