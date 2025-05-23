Question: Where is the video taken?

Reference Answer: 1

Video ID: 4088558209

Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="Where is the video taken?")
ANSWER0=SELECT(question="Where is the video taken?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is the video taken?')=<b><span style='color: green;'>The video is taken on a stage.</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is the video taken?, <b><span style='color: darkorange;'>information</span></b>=['The video is taken on a stage.'], <b><span style='color: darkorange;'>choices</span></b>=['in house', 'stage', 'carnival', 'outdoors', 'park'])=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

