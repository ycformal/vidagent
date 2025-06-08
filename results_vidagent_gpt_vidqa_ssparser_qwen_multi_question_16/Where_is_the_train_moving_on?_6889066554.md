Question: Where is the train moving on?

Reference Answer: 4

Video ID: 6889066554

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is the train moving?|What is the train moving on?|What is the train's destination?|What is the train's route?|What is the train's direction?|What is the train's speed?|What is the train's location in relation to other objects?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is the train moving?|What is the train moving on?|What is the train's destination?|What is the train's route?|What is the train's direction?|What is the train's speed?|What is the train's location in relation to other objects?")
SELECTED=SELECT(question="Where is the train moving on?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is the train moving?|What is the train moving on?|What is the train's destination?|What is the train's route?|What is the train's direction?|What is the train's speed?|What is the train's location in relation to other objects?')=<b><span style='color: green;'>User: Where is the train moving on?
Assistant: The train is moving on the tracks.

User: What is the train moving on?
Assistant: The train is moving on a railway track.

User: What is the train's destination?
Assistant: The train's destination is not specified in the video caption.

User: What is the train's route?
Assistant: The train is traveling on a railway track, moving steadily forward.

User: What is the train's direction?
Assistant: The train is moving towards the camera.

User: What is the train's speed?
Assistant: The train is moving slowly.

User: What is the train's location in relation to other objects?
Assistant: The train is on the tracks, surrounded by grassy areas, trees, and buildings.

Note: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is the train moving on?, <b><span style='color: darkorange;'>information</span></b>=["User: Where is the train moving on?\nAssistant: The train is moving on the tracks.\n\nUser: What is the train moving on?\nAssistant: The train is moving on a railway track.\n\nUser: What is the train's destination?\nAssistant: The train's destination is not specified in the video caption.\n\nUser: What is the train's route?\nAssistant: The train is traveling on a railway track, moving steadily forward.\n\nUser: What is the train's direction?\nAssistant: The train is moving towards the camera.\n\nUser: What is the train's speed?\nAssistant: The train is moving slowly.\n\nUser: What is the train's location in relation to other objects?\nAssistant: The train is on the tracks, surrounded by grassy areas, trees, and buildings.\n\nNote: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant."], <b><span style='color: darkorange;'>choices</span></b>=['carpark', 'baby trolley', 'footpath', 'jungle', 'train railway'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

