Question: Where is the girl hanging out?

Reference Answer: 0

Video ID: 7957216542

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is the girl hanging out?|Where is the girl located?|What is the girl doing?|What surrounds the girl?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is the girl hanging out?|Where is the girl located?|What is the girl doing?|What surrounds the girl?")
SELECTED=SELECT(question="Where is the girl hanging out?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Where is the girl hanging out?|Where is the girl located?|What is the girl doing?|What surrounds the girl?')=<b><span style='color: green;'>User: Where is the girl hanging out?
Assistant: reading corner.

User: Where is the girl located?
Assistant: The girl is sitting on a large, plush, white chair that resembles a sheep.

User: What is the girl doing?
Assistant: The girl is deeply engaged in reading a colorful book.

User: What surrounds the girl?
Assistant: The girl is surrounded by a wooden bookshelf filled with books, a colorful alphabet toy, and other toys scattered on the floor.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is the girl hanging out?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is the girl hanging out?\nAssistant: reading corner.\n\nUser: Where is the girl located?\nAssistant: The girl is sitting on a large, plush, white chair that resembles a sheep.\n\nUser: What is the girl doing?\nAssistant: The girl is deeply engaged in reading a colorful book.\n\nUser: What surrounds the girl?\nAssistant: The girl is surrounded by a wooden bookshelf filled with books, a colorful alphabet toy, and other toys scattered on the floor.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['reading corner', 'chairs', 'living area', 'mountains', 'mat'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

