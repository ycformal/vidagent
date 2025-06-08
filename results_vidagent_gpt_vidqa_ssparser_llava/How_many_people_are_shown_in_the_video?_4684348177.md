Question: How many people are shown in the video?

Reference Answer: 4

Video ID: 4684348177

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people are shown in the video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people are shown in the video?")
SELECTED=SELECT(question="How many people are shown in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many people are shown in the video?')=<b><span style='color: green;'>USER: 
How many people are shown in the video?
Choices (choose one): five, one, four, three, two ASSISTANT: There are two people shown in the video.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are shown in the video?, <b><span style='color: darkorange;'>information</span></b>=['USER: \nHow many people are shown in the video?\nChoices (choose one): five, one, four, three, two ASSISTANT: There are two people shown in the video.'], <b><span style='color: darkorange;'>choices</span></b>=['five', 'one', 'four', 'three', 'two'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

