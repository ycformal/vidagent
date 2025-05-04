Question: How many cats are there in the video?

Reference Answer: 4

Video ID: 7730642486

Program:

```
ANSWERS0=VQA(video=VIDEO,question="How many cats are there?")
ANSWER0=SELECT(question="How many cats are there in the video?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many cats are there?')=<b><span style='color: green;'>['2', '1', '1', '2', '3', '2', '2', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '3', '2', '2', '2', '3', '1', '4', '3', '3', '2', '2', '3']</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many cats are there in the video?, <b><span style='color: darkorange;'>information</span></b>=['2', '1', '1', '2', '3', '2', '2', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '3', '2', '2', '2', '3', '1', '4', '3', '3', '2', '2', '3'], <b><span style='color: darkorange;'>choices</span></b>=['four', 'two', 'five', 'one', 'three'])=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

