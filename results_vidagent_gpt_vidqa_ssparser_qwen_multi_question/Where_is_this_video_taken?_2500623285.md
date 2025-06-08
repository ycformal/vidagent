Question: Where is this video taken?

Reference Answer: 4

Video ID: 2500623285

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where does the action in the video take place?|What is the background of the video?|What landmarks or objects can be seen in the video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where does the action in the video take place?|What is the background of the video?|What landmarks or objects can be seen in the video?")
SELECTED=SELECT(question="Where is this video taken?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where does the action in the video take place?|What is the background of the video?|What landmarks or objects can be seen in the video?')=<b><span style='color: green;'>User: Where is this video taken?
Assistant: The video is taken in a living room.

User: What is the location of the video?
Assistant: The video is set in a living room.

User: What is the setting of the video?
Assistant: The setting of the video is a room with a carpeted floor and a piece of furniture in the background.

User: Where does the action in the video take place?
Assistant: The action takes place in a living room.

User: What is the background of the video?
Assistant: The background of the video is a carpeted floor with a storage box visible.

User: What landmarks or objects can be seen in the video?
Assistant: The video shows a child playing with a toy car, a box, and a tripod.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this video taken?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this video taken?\nAssistant: The video is taken in a living room.\n\nUser: What is the location of the video?\nAssistant: The video is set in a living room.\n\nUser: What is the setting of the video?\nAssistant: The setting of the video is a room with a carpeted floor and a piece of furniture in the background.\n\nUser: Where does the action in the video take place?\nAssistant: The action takes place in a living room.\n\nUser: What is the background of the video?\nAssistant: The background of the video is a carpeted floor with a storage box visible.\n\nUser: What landmarks or objects can be seen in the video?\nAssistant: The video shows a child playing with a toy car, a box, and a tripod.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['indoors', 'kitchen', 'stage', 'road', 'beach'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

