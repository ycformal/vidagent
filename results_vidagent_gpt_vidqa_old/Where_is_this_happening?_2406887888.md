Question: Where is this happening?

Reference Answer: 2

Video ID: 2406887888

Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="Where is this happening?")
ANSWER0=SELECT(question="Where is this happening?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this happening?')=<b><span style='color: green;'>USER: 
Where is this happening? ASSISTANT: 




 
 
 
 </span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this happening?, <b><span style='color: darkorange;'>information</span></b>=['USER: \nWhere is this happening? ASSISTANT: \n\n\n\n\n \n \n \n '], <b><span style='color: darkorange;'>choices</span></b>=['swimming pool', 'garden', 'living room', 'trail', 'on the road'])=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

