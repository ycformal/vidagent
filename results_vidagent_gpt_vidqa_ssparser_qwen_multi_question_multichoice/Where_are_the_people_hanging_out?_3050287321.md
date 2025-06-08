Question: Where are the people hanging out?

Reference Answer: 3

Video ID: 3050287321

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where are the people hanging out?|Where is the location of the people?|What is the setting of the video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where are the people hanging out?|Where is the location of the people?|What is the setting of the video?")
SELECTED=SELECT(question="Where are the people hanging out?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where are the people hanging out?|Where is the location of the people?|What is the setting of the video?')=<b><span style='color: green;'>User: Where are the people hanging out?
Assistant: swimming pool.

User: Where is the location of the people?
Assistant: The people are in a room.

User: What is the setting of the video?
Assistant: The setting of the video is a dark background with a horizontal gray line at the bottom, resembling a television screen.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where are the people hanging out?, <b><span style='color: darkorange;'>information</span></b>=['User: Where are the people hanging out?\nAssistant: swimming pool.\n\nUser: Where is the location of the people?\nAssistant: The people are in a room.\n\nUser: What is the setting of the video?\nAssistant: The setting of the video is a dark background with a horizontal gray line at the bottom, resembling a television screen.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['snow mountain', 'zoo', 'swimming pool', 'bedroom', 'beach'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

