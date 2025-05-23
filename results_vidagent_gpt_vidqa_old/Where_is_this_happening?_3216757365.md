Question: Where is this happening?

Reference Answer: 0

Video ID: 3216757365

Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="Where is this happening?")
ANSWER0=SELECT(question="Where is this happening?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this happening?')=<b><span style='color: green;'>USER: 
Where is this happening? ASSISTANT: 
















































</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this happening?, <b><span style='color: darkorange;'>information</span></b>=['USER: \nWhere is this happening? ASSISTANT: \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['porch', 'forest', 'hiking', 'outdoors', 'in the sea'])=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>3</span></b></div><hr>

Answer: 3

