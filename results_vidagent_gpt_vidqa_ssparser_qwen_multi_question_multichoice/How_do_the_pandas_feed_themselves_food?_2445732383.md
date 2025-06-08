Question: How do the pandas feed themselves food?

Reference Answer: 0

Video ID: 2445732383

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How do the pandas feed themselves food?|What are the pandas doing?|What surrounds the pandas?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How do the pandas feed themselves food?|What are the pandas doing?|What surrounds the pandas?")
SELECTED=SELECT(question="How do the pandas feed themselves food?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How do the pandas feed themselves food?|What are the pandas doing?|What surrounds the pandas?')=<b><span style='color: green;'>User: How do the pandas feed themselves food?
Assistant: using paws

User: What are the pandas doing?
Assistant: The pandas are eating bamboo.

User: What surrounds the pandas?
Assistant: The pandas are surrounded by a dense forest of bamboo.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How do the pandas feed themselves food?, <b><span style='color: darkorange;'>information</span></b>=['User: How do the pandas feed themselves food?\nAssistant: using paws\n\nUser: What are the pandas doing?\nAssistant: The pandas are eating bamboo.\n\nUser: What surrounds the pandas?\nAssistant: The pandas are surrounded by a dense forest of bamboo.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['using paws', 'put food in hands', 'lying on the mattress', 'drink', 'with its trunk'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

