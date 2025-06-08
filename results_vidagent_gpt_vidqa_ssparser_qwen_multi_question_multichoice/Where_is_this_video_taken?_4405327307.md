Question: Where is this video taken?

Reference Answer: 4

Video ID: 4405327307

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
Assistant: The video is set on a stage with a live band performance.

User: Where was this video recorded?
Assistant: The video was recorded on a stage.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this video taken?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this video taken?\nAssistant: stage.\n\nUser: What is the location of this video?\nAssistant: The video is set on a stage with a live band performance.\n\nUser: Where was this video recorded?\nAssistant: The video was recorded on a stage.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['snow mountain', 'road', 'dancing hall', 'ball room', 'stage'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

