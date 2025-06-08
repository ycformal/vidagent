Question: How did the lady support herself on the seesaw?

Reference Answer: 1

Video ID: 2814476910

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How did the lady support herself on the seesaw?|What is the lady doing on the seesaw?|What is the lady's body position on the seesaw?|What is the lady's reaction to the seesaw?|Is the lady using any objects to support herself on the seesaw?|What is the lady's facial expression while on the seesaw?|How does the lady's position change while on the seesaw?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How did the lady support herself on the seesaw?|What is the lady doing on the seesaw?|What is the lady's body position on the seesaw?|What is the lady's reaction to the seesaw?|Is the lady using any objects to support herself on the seesaw?|What is the lady's facial expression while on the seesaw?|How does the lady's position change while on the seesaw?")
SELECTED=SELECT(question="How did the lady support herself on the seesaw?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How did the lady support herself on the seesaw?|What is the lady doing on the seesaw?|What is the lady's body position on the seesaw?|What is the lady's reaction to the seesaw?|Is the lady using any objects to support herself on the seesaw?|What is the lady's facial expression while on the seesaw?|How does the lady's position change while on the seesaw?')=<b><span style='color: green;'>User: How did the lady support herself on the seesaw?
Assistant: The lady supported herself with her hands on the ground.

User: What is the lady doing on the seesaw?
Assistant: The lady is sitting on the seesaw.

User: What is the lady's body position on the seesaw?
Assistant: The lady is sitting on the left side of the seesaw.

User: What is the lady's reaction to the seesaw?
Assistant: The lady is laughing.

User: Is the lady using any objects to support herself on the seesaw?
Assistant: No, the lady is not using any objects to support herself on the seesaw.

User: What is the lady's facial expression while on the seesaw?
Assistant: The lady has a joyful expression on her face.

User: How does the lady's position change while on the seesaw?
Assistant: The lady's position changes from being on the left side of the seesaw to being on the right side.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How did the lady support herself on the seesaw?, <b><span style='color: darkorange;'>information</span></b>=["User: How did the lady support herself on the seesaw?\nAssistant: The lady supported herself with her hands on the ground.\n\nUser: What is the lady doing on the seesaw?\nAssistant: The lady is sitting on the seesaw.\n\nUser: What is the lady's body position on the seesaw?\nAssistant: The lady is sitting on the left side of the seesaw.\n\nUser: What is the lady's reaction to the seesaw?\nAssistant: The lady is laughing.\n\nUser: Is the lady using any objects to support herself on the seesaw?\nAssistant: No, the lady is not using any objects to support herself on the seesaw.\n\nUser: What is the lady's facial expression while on the seesaw?\nAssistant: The lady has a joyful expression on her face.\n\nUser: How does the lady's position change while on the seesaw?\nAssistant: The lady's position changes from being on the left side of the seesaw to being on the right side.\n\n"], <b><span style='color: darkorange;'>choices</span></b>=['hold ski stick', 'legs on the floor', 'wear life jacket', 'hold up cup', 'from her hand'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

