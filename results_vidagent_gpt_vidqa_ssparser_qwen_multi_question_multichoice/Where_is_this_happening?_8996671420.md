Question: Where is this happening?

Reference Answer: 0

Video ID: 8996671420

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this happening?|Where is the location of this event?|Where is the setting of this video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this happening?|Where is the location of this event?|Where is the setting of this video?")
SELECTED=SELECT(question="Where is this happening?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this happening?|Where is the location of this event?|Where is the setting of this video?')=<b><span style='color: green;'>User: Where is this happening?
Assistant: underpass

User: Where is the location of this event?
Assistant: The location of this event is a well-lit, spacious corridor, likely within an airport or a similar transit hub.

User: Where is the setting of this video?
Assistant: The setting of the video is a well-lit, clean, and spacious corridor, likely within an airport or a similar transit hub.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this happening?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this happening?\nAssistant: underpass\n\nUser: Where is the location of this event?\nAssistant: The location of this event is a well-lit, spacious corridor, likely within an airport or a similar transit hub.\n\nUser: Where is the setting of this video?\nAssistant: The setting of the video is a well-lit, clean, and spacious corridor, likely within an airport or a similar transit hub.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['underpass', 'in the day', 'swimming pool', 'room', 'playground'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

