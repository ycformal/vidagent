Question: Where are the people playing the sport?

Reference Answer: 1

Video ID: 5552394033

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where are the people playing the sport?|What is the location of the people playing the sport?|What surrounds the people playing the sport?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where are the people playing the sport?|What is the location of the people playing the sport?|What surrounds the people playing the sport?")
SELECTED=SELECT(question="Where are the people playing the sport?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where are the people playing the sport?|What is the location of the people playing the sport?|What surrounds the people playing the sport?')=<b><span style='color: green;'>User: Where are the people playing the sport?
Assistant: park

User: What is the location of the people playing the sport?
Assistant: The people are playing the sport on a grassy field in a suburban area.

User: What surrounds the people playing the sport?
Assistant: The people are surrounded by a grassy field, trees, and parked cars.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where are the people playing the sport?, <b><span style='color: darkorange;'>information</span></b>=['User: Where are the people playing the sport?\nAssistant: park\n\nUser: What is the location of the people playing the sport?\nAssistant: The people are playing the sport on a grassy field in a suburban area.\n\nUser: What surrounds the people playing the sport?\nAssistant: The people are surrounded by a grassy field, trees, and parked cars.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['stage', 'grass patch', 'park', 'side of a road', 'sports hall'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

