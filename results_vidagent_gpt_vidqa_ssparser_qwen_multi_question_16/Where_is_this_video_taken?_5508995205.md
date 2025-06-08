Question: Where is this video taken?

Reference Answer: 2

Video ID: 5508995205

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where are the people in the video?|What is the background of the video?|What landmarks or objects can be seen in the video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where are the people in the video?|What is the background of the video?|What landmarks or objects can be seen in the video?")
SELECTED=SELECT(question="Where is this video taken?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where are the people in the video?|What is the background of the video?|What landmarks or objects can be seen in the video?')=<b><span style='color: green;'>User: Where is this video taken?
Assistant: The video is taken in an indoor swimming pool.

User: What is the location of the video?
Assistant: The video takes place in an indoor swimming pool.

User: What is the setting of the video?
Assistant: The video is set in an indoor swimming pool with clear blue water and lane dividers.

User: Where are the people in the video?
Assistant: The people are in a swimming pool.

User: What is the background of the video?
Assistant: The background of the video is a typical indoor swimming pool with lane dividers and other swimmers in the distance.

User: What landmarks or objects can be seen in the video?
Assistant: The video shows a swimming pool with lane dividers and other swimmers in the background.

Note: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this video taken?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this video taken?\nAssistant: The video is taken in an indoor swimming pool.\n\nUser: What is the location of the video?\nAssistant: The video takes place in an indoor swimming pool.\n\nUser: What is the setting of the video?\nAssistant: The video is set in an indoor swimming pool with clear blue water and lane dividers.\n\nUser: Where are the people in the video?\nAssistant: The people are in a swimming pool.\n\nUser: What is the background of the video?\nAssistant: The background of the video is a typical indoor swimming pool with lane dividers and other swimmers in the distance.\n\nUser: What landmarks or objects can be seen in the video?\nAssistant: The video shows a swimming pool with lane dividers and other swimmers in the background.\n\nNote: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.'], <b><span style='color: darkorange;'>choices</span></b>=['stage', 'along the streets', 'swimming pool', 'playground', 'speech event'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

