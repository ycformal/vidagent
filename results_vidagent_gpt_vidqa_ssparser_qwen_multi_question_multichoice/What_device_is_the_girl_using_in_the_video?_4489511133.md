Question: What device is the girl using in the video?

Reference Answer: 1

Video ID: 4489511133

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="What device is the girl using?|What is the girl doing?|What surrounds the girl?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="What device is the girl using?|What is the girl doing?|What surrounds the girl?")
SELECTED=SELECT(question="What device is the girl using in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='What device is the girl using?|What is the girl doing?|What surrounds the girl?')=<b><span style='color: green;'>User: What device is the girl using in the video?
Assistant: phone.

User: What is the girl doing?
Assistant: The girl is intently focused on a smartphone placed on a black metal mesh surface.

User: What surrounds the girl?
Assistant: The girl is surrounded by a black metal mesh surface, likely part of a playground or outdoor seating area.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What device is the girl using in the video?, <b><span style='color: darkorange;'>information</span></b>=['User: What device is the girl using in the video?\nAssistant: phone.\n\nUser: What is the girl doing?\nAssistant: The girl is intently focused on a smartphone placed on a black metal mesh surface.\n\nUser: What surrounds the girl?\nAssistant: The girl is surrounded by a black metal mesh surface, likely part of a playground or outdoor seating area.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['tablet', 'phone', 'camera', 'video film', 'polaroid'])=<b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

