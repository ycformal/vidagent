Question: How many people are there in the video?

Reference Answer: 1

Video ID: 6764465247

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people are there?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people are there?")
SELECTED=SELECT(question="How many people are there in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many people are there?')=<b><span style='color: green;'>USER: 
How many people are there in the video?
Choices (choose one): one, two, three, thirteen, nine ASSISTANT: Two</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are there in the video?, <b><span style='color: darkorange;'>information</span></b>=['USER: \nHow many people are there in the video?\nChoices (choose one): one, two, three, thirteen, nine ASSISTANT: Two'], <b><span style='color: darkorange;'>choices</span></b>=['one', 'two', 'three', 'thirteen', 'nine'])=<b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

