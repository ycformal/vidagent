Question: Why was there white smoke on the sky?

Reference Answer: 0

Video ID: 2639154995

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Why was there white smoke in the sky?|What caused the white smoke in the sky?|What is the source of the white smoke?|What is the color of the smoke?|What is the shape of the smoke?|How does the smoke move in the sky?|What is the location of the smoke in the sky?|What is the weather like when the smoke appears?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Why was there white smoke in the sky?|What caused the white smoke in the sky?|What is the source of the white smoke?|What is the color of the smoke?|What is the shape of the smoke?|How does the smoke move in the sky?|What is the location of the smoke in the sky?|What is the weather like when the smoke appears?")
SELECTED=SELECT(question="Why was there white smoke on the sky?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='Why was there white smoke in the sky?|What caused the white smoke in the sky?|What is the source of the white smoke?|What is the color of the smoke?|What is the shape of the smoke?|How does the smoke move in the sky?|What is the location of the smoke in the sky?|What is the weather like when the smoke appears?')=<b><span style='color: green;'>User: Why was there white smoke on the sky?
Assistant: The white smoke was caused by the fireworks.

User: What caused the white smoke in the sky?
Assistant: The white smoke in the sky was caused by the fireworks.

User: What is the source of the white smoke?
Assistant: The white smoke is from the fireworks.

User: What is the color of the smoke?
Assistant: The smoke is white.

User: What is the shape of the smoke?
Assistant: The smoke is in the shape of a circle.

User: How does the smoke move in the sky?
Assistant: The smoke from the fireworks disperses slowly in the sky.

User: What is the location of the smoke in the sky?
Assistant: The smoke from the fireworks is visible in the sky, adding to the festive atmosphere.

User: What is the weather like when the smoke appears?
Assistant: The smoke appears to be light and wispy, suggesting a mild breeze.

Note: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Why was there white smoke on the sky?, <b><span style='color: darkorange;'>information</span></b>=['User: Why was there white smoke on the sky?\nAssistant: The white smoke was caused by the fireworks.\n\nUser: What caused the white smoke in the sky?\nAssistant: The white smoke in the sky was caused by the fireworks.\n\nUser: What is the source of the white smoke?\nAssistant: The white smoke is from the fireworks.\n\nUser: What is the color of the smoke?\nAssistant: The smoke is white.\n\nUser: What is the shape of the smoke?\nAssistant: The smoke is in the shape of a circle.\n\nUser: How does the smoke move in the sky?\nAssistant: The smoke from the fireworks disperses slowly in the sky.\n\nUser: What is the location of the smoke in the sky?\nAssistant: The smoke from the fireworks is visible in the sky, adding to the festive atmosphere.\n\nUser: What is the weather like when the smoke appears?\nAssistant: The smoke appears to be light and wispy, suggesting a mild breeze.\n\nNote: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.'], <b><span style='color: darkorange;'>choices</span></b>=['from the fireworks', 'airline flew past', 'fire', 'camera tricks', 'chimney smoke'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

