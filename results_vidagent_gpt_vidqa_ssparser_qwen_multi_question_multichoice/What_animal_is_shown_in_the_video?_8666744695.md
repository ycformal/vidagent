Question: What animal is shown in the video?

Reference Answer: 2

Video ID: 8666744695

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="What animal is shown in the video?|What is the animal doing?|What surrounds the animal?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="What animal is shown in the video?|What is the animal doing?|What surrounds the animal?")
SELECTED=SELECT(question="What animal is shown in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='What animal is shown in the video?|What is the animal doing?|What surrounds the animal?')=<b><span style='color: green;'>User: What animal is shown in the video?
Assistant: dog

User: What is the animal doing?
Assistant: The animal is moving around the room, sniffing the floor and exploring its surroundings.

User: What surrounds the animal?
Assistant: The animal is surrounded by a cardboard box filled with papers and a blue and white radio on the floor.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What animal is shown in the video?, <b><span style='color: darkorange;'>information</span></b>=['User: What animal is shown in the video?\nAssistant: dog\n\nUser: What is the animal doing?\nAssistant: The animal is moving around the room, sniffing the floor and exploring its surroundings.\n\nUser: What surrounds the animal?\nAssistant: The animal is surrounded by a cardboard box filled with papers and a blue and white radio on the floor.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['elephants', 'tiger', 'dog', 'fish', 'elephant'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

