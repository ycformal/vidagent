Question: How many people are performing on the stage?

Reference Answer: 2

Video ID: 2836465095

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people are performing on the stage?|How many performers are there?|How many people are on the stage?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people are performing on the stage?|How many performers are there?|How many people are on the stage?")
SELECTED=SELECT(question="How many people are performing on the stage?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many people are performing on the stage?|How many performers are there?|How many people are on the stage?')=<b><span style='color: green;'>User: How many people are performing on the stage?
Assistant: two.

User: How many performers are there?
Assistant: There are two performers.

User: How many people are on the stage?
Assistant: There are two people on the stage.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are performing on the stage?, <b><span style='color: darkorange;'>information</span></b>=['User: How many people are performing on the stage?\nAssistant: two.\n\nUser: How many performers are there?\nAssistant: There are two performers.\n\nUser: How many people are on the stage?\nAssistant: There are two people on the stage.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['four', 'nine', 'two', 'six', 'five'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

