Question: Where is this?

Reference Answer: 4

Video ID: 8340480194

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this?|What location is this?|What is the setting of this video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this?|What location is this?|What is the setting of this video?")
SELECTED=SELECT(question="Where is this?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this?|What location is this?|What is the setting of this video?')=<b><span style='color: green;'>User: Where is this?
Assistant: home.

User: What location is this?
Assistant: This is a living room.

User: What is the setting of this video?
Assistant: The setting of the video is a cozy living room with a beige couch, a colorful pillow, a striped dog bed, and a small round table.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this?\nAssistant: home.\n\nUser: What location is this?\nAssistant: This is a living room.\n\nUser: What is the setting of this video?\nAssistant: The setting of the video is a cozy living room with a beige couch, a colorful pillow, a striped dog bed, and a small round table.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['outdoor', 'factory', 'hospital room', 'playground', 'home'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

