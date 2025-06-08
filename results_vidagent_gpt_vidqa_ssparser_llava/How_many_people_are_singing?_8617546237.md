Question: How many people are singing?

Reference Answer: 3

Video ID: 8617546237

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people are singing?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people are singing?")
SELECTED=SELECT(question="How many people are singing?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many people are singing?')=<b><span style='color: green;'>USER: 
How many people are singing?
Choices (choose one): eleven, two, one, four, three ASSISTANT: Three</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are singing?, <b><span style='color: darkorange;'>information</span></b>=['USER: \nHow many people are singing?\nChoices (choose one): eleven, two, one, four, three ASSISTANT: Three'], <b><span style='color: darkorange;'>choices</span></b>=['eleven', 'two', 'one', 'four', 'three'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

