Question: How do they warm up?

Reference Answer: 4

Video ID: 3584252430

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How do they warm up?|What are they doing to warm up?|What surrounds them?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How do they warm up?|What are they doing to warm up?|What surrounds them?")
SELECTED=SELECT(question="How do they warm up?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How do they warm up?|What are they doing to warm up?|What surrounds them?')=<b><span style='color: green;'>User: How do they warm up?
Assistant: stretch hands out.

User: What are they doing to warm up?
Assistant: They are performing stretching exercises.

User: What surrounds them?
Assistant: They are surrounded by colorful benches and various items of clothing scattered on the ground.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How do they warm up?, <b><span style='color: darkorange;'>information</span></b>=['User: How do they warm up?\nAssistant: stretch hands out.\n\nUser: What are they doing to warm up?\nAssistant: They are performing stretching exercises.\n\nUser: What surrounds them?\nAssistant: They are surrounded by colorful benches and various items of clothing scattered on the ground.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['wear thick clothings', 'wear sweater and jacket', 'heater', 'winter clothing', 'stretch hands out'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

