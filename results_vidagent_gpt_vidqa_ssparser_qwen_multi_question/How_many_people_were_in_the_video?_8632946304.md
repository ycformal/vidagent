Question: How many people were in the video?

Reference Answer: 1

Video ID: 8632946304

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people were in the video?|How many individuals appear in the video?|What is the total number of people in the video?|How many people can be seen in the video?|What is the headcount of people in the video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people were in the video?|How many individuals appear in the video?|What is the total number of people in the video?|How many people can be seen in the video?|What is the headcount of people in the video?")
SELECTED=SELECT(question="How many people were in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many people were in the video?|How many individuals appear in the video?|What is the total number of people in the video?|How many people can be seen in the video?|What is the headcount of people in the video?')=<b><span style='color: green;'>User: How many people were in the video?
Assistant: There were three people in the video: a child on a scooter, an adult, and another child on roller skates.

User: How many individuals appear in the video?
Assistant: Three individuals appear in the video: a child on a scooter, an adult, and another child on roller skates.

User: What is the total number of people in the video?
Assistant: There are three people in the video: a child on a scooter, an adult, and another child on roller skates.

User: How many people can be seen in the video?
Assistant: Three people can be seen in the video: a child on a scooter, an adult, and another child on roller skates.

User: What is the headcount of people in the video?
Assistant: There are three people in the video: a child on a scooter, an adult, and another child on roller skates.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people were in the video?, <b><span style='color: darkorange;'>information</span></b>=['User: How many people were in the video?\nAssistant: There were three people in the video: a child on a scooter, an adult, and another child on roller skates.\n\nUser: How many individuals appear in the video?\nAssistant: Three individuals appear in the video: a child on a scooter, an adult, and another child on roller skates.\n\nUser: What is the total number of people in the video?\nAssistant: There are three people in the video: a child on a scooter, an adult, and another child on roller skates.\n\nUser: How many people can be seen in the video?\nAssistant: Three people can be seen in the video: a child on a scooter, an adult, and another child on roller skates.\n\nUser: What is the headcount of people in the video?\nAssistant: There are three people in the video: a child on a scooter, an adult, and another child on roller skates.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['one', 'three', 'four', 'two', 'nine'])=<b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

