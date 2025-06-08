Question: Where is this video taken?

Reference Answer: 4

Video ID: 2500623285

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
Assistant: indoor

User: What is the location of this video?
Assistant: The video is set in a room with a carpeted floor and a piece of furniture, possibly a couch or a bed.

User: Where was this video recorded?
Assistant: The video was recorded in a living room.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this video taken?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this video taken?\nAssistant: indoor\n\nUser: What is the location of this video?\nAssistant: The video is set in a room with a carpeted floor and a piece of furniture, possibly a couch or a bed.\n\nUser: Where was this video recorded?\nAssistant: The video was recorded in a living room.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['indoors', 'kitchen', 'stage', 'road', 'beach'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

