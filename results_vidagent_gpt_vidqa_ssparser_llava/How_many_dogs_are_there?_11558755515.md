Question: How many dogs are there?

Reference Answer: 0

Video ID: 11558755515

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many dogs are there?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many dogs are there?")
SELECTED=SELECT(question="How many dogs are there?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many dogs are there?')=<b><span style='color: green;'>USER: 
How many dogs are there?
Choices (choose one): two, nine, one, four, three ASSISTANT: There are two dogs in the image.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many dogs are there?, <b><span style='color: darkorange;'>information</span></b>=['USER: \nHow many dogs are there?\nChoices (choose one): two, nine, one, four, three ASSISTANT: There are two dogs in the image.'], <b><span style='color: darkorange;'>choices</span></b>=['two', 'nine', 'one', 'four', 'three'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

