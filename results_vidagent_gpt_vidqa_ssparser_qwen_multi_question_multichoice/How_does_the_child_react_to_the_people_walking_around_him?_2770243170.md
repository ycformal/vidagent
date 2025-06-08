Question: How does the child react to the people walking around him?

Reference Answer: 2

Video ID: 2770243170

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How does the child react to the people walking around him?|What is the child doing?|What surrounds the child?|How is the child feeling?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How does the child react to the people walking around him?|What is the child doing?|What surrounds the child?|How is the child feeling?")
SELECTED=SELECT(question="How does the child react to the people walking around him?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How does the child react to the people walking around him?|What is the child doing?|What surrounds the child?|How is the child feeling?')=<b><span style='color: green;'>User: How does the child react to the people walking around him?
Assistant: looking around

User: What is the child doing?
Assistant: The child is standing in a pink baby walker, holding onto the walker's tray and occasionally looking around.

User: What surrounds the child?
Assistant: The child is surrounded by a pink walker with four wheels, a pink cushioned seat with a floral pattern, and three colorful balls (two red and one blue) on the tray.

User: How is the child feeling?
Assistant: The child appears to be curious and engaged with the walker.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How does the child react to the people walking around him?, <b><span style='color: darkorange;'>information</span></b>=["User: How does the child react to the people walking around him?\nAssistant: looking around\n\nUser: What is the child doing?\nAssistant: The child is standing in a pink baby walker, holding onto the walker's tray and occasionally looking around.\n\nUser: What surrounds the child?\nAssistant: The child is surrounded by a pink walker with four wheels, a pink cushioned seat with a floral pattern, and three colorful balls (two red and one blue) on the tray.\n\nUser: How is the child feeling?\nAssistant: The child appears to be curious and engaged with the walker.\n\n"], <b><span style='color: darkorange;'>choices</span></b>=['wathc seriously', 'blow candle', 'looking around', 'happy', 'singing'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

