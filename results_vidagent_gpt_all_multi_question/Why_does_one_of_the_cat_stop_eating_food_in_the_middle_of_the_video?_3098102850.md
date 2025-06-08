Question: Why does one of the cat stop eating food in the middle of the video?

Reference Answer: 4

Video ID: 3098102850

Original program:

```
TIME=FLAG(begin=None,middle="in the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="One of the cats has stopped eating food.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="Why did one of the cats stop eating food?|What is the cat's behavior before stopping?|Is the cat eating alone or with other cats?|What is the cat's body language while eating?|What is the cat's reaction to the food?|Is the cat distracted by something?|What is the environment around the cat while eating?")
```

Program:

```
TIME=FLAG(begin=None,middle="in the [middle] of",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="One of the cats has stopped eating food.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="Why did one of the cats stop eating food?|What is the cat's behavior before stopping?|Is the cat eating alone or with other cats?|What is the cat's body language while eating?|What is the cat's reaction to the food?|Is the cat distracted by something?|What is the environment around the cat while eating?")
```

Answer: 4

