Question: What does the baby hold in his left hand as he is playing with the purple bowl in the middle?

Reference Answer: 2

Video ID: 9214485291

Original program:

```
TIME=FLAG(begin=None,middle="in the [middle]",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The baby is playing with the purple bowl.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the baby holding in his left hand?|What is the baby's posture while holding the object?|Is the baby interacting with the object in any way?|What is the size and shape of the object?|Is the object related to the purple bowl?|What is the baby's facial expression while holding the object?")
```

Program:

```
TIME=FLAG(begin=None,middle="in the [middle]",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The baby is playing with the purple bowl.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What is the baby holding in his left hand?|What is the baby's posture while holding the object?|Is the baby interacting with the object in any way?|What is the size and shape of the object?|Is the object related to the purple bowl?|What is the baby's facial expression while holding the object?")
```

Answer: 2

