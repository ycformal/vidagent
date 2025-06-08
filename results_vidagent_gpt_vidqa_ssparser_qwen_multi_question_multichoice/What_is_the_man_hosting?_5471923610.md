Question: What is the man hosting?

Reference Answer: 3

Video ID: 5471923610

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="What is the man hosting?|What is the event being hosted?|What is the man doing?|What surrounds the man?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="What is the man hosting?|What is the event being hosted?|What is the man doing?|What surrounds the man?")
SELECTED=SELECT(question="What is the man hosting?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='What is the man hosting?|What is the event being hosted?|What is the man doing?|What surrounds the man?')=<b><span style='color: green;'>User: What is the man hosting?
Assistant: game show

User: What is the event being hosted?
Assistant: The event being hosted is a game show.

User: What is the man doing?
Assistant: The man is standing behind a podium, reading from a script or notes.

User: What surrounds the man?
Assistant: The man is surrounded by a large screen displaying various monetary amounts in yellow text on a dark background, and a podium with a transparent front.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What is the man hosting?, <b><span style='color: darkorange;'>information</span></b>=['User: What is the man hosting?\nAssistant: game show\n\nUser: What is the event being hosted?\nAssistant: The event being hosted is a game show.\n\nUser: What is the man doing?\nAssistant: The man is standing behind a podium, reading from a script or notes.\n\nUser: What surrounds the man?\nAssistant: The man is surrounded by a large screen displaying various monetary amounts in yellow text on a dark background, and a podium with a transparent front.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['referee', 'prototype of a hot air balloon', 'parent offspring', 'game show', 'foosball'])=<b><span style='color: green;'>3</span></b></div><hr>

Answer: 3

