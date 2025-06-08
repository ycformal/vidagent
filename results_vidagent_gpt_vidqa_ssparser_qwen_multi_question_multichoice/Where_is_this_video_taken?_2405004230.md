Question: Where is this video taken?

Reference Answer: 3

Video ID: 2405004230

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this video taken?|What is the location of this video?|Where was this video recorded?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this video taken?|What is the location of this video?|Where was this video recorded?")
SELECTED=SELECT(question="Where is this video taken?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this video taken?|What is the location of this video?|Where was this video recorded?')=<b><span style='color: green;'>User: Where is this video taken?
Assistant: stage.

User: What is the location of this video?
Assistant: The video is set at the Crystal Geyser stage.

User: Where was this video recorded?
Assistant: The video was recorded at the Crystal Geyser stage.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this video taken?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this video taken?\nAssistant: stage.\n\nUser: What is the location of this video?\nAssistant: The video is set at the Crystal Geyser stage.\n\nUser: Where was this video recorded?\nAssistant: The video was recorded at the Crystal Geyser stage.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['stage', 'ball room', 'by a lake', 'carnival', 'room'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

