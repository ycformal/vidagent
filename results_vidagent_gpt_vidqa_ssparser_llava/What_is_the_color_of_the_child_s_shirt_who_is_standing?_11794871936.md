Question: What is the color of the child s shirt who is standing?

Reference Answer: 2

Video ID: 11794871936

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="What is the color of the child's shirt who is standing?|What is the child wearing?|What surrounds the child?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="What is the color of the child's shirt who is standing?|What is the child wearing?|What surrounds the child?")
SELECTED=SELECT(question="What is the color of the child s shirt who is standing?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='What is the color of the child's shirt who is standing?|What is the child wearing?|What surrounds the child?')=<b><span style='color: green;'>USER: 
What is the color of the child s shirt who is standing?
Choices (choose one): green, light blue, black, pink, white ASSISTANT: The child standing is wearing a black shirt.
USER: 
What is the child wearing? ASSISTANT: The child is wearing a black shirt.
USER: 
What surrounds the child? ASSISTANT: The child is surrounded by a woman who is holding them and a couch. The woman appears to be sitting on the couch, and there are some items in the background that suggest a living room setting, such as a lamp, a bookshelf, and a window. The child is wearing a white outfit and seems to be looking at the camera with a curious or content expression.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What is the color of the child s shirt who is standing?, <b><span style='color: darkorange;'>information</span></b>=['USER: \nWhat is the color of the child s shirt who is standing?\nChoices (choose one): green, light blue, black, pink, white ASSISTANT: The child standing is wearing a black shirt.\nUSER: \nWhat is the child wearing? ASSISTANT: The child is wearing a black shirt.\nUSER: \nWhat surrounds the child? ASSISTANT: The child is surrounded by a woman who is holding them and a couch. The woman appears to be sitting on the couch, and there are some items in the background that suggest a living room setting, such as a lamp, a bookshelf, and a window. The child is wearing a white outfit and seems to be looking at the camera with a curious or content expression.'], <b><span style='color: darkorange;'>choices</span></b>=['green', 'light blue', 'black', 'pink', 'white'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

