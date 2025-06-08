Question: What did the orange cat do after the brown cat found food?

Reference Answer: 2

Video ID: 9289576155

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The brown cat has found food.")
VIDEO0=CLIP_AFTER(video=VIDEO,frame=FRAME0)
FRAME1=LOC(video=VIDEO0,event="The orange cat is doing something.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME1)
ANSWERS0=VQA(video=VIDEO1,question="What is the orange cat doing?|What is the orange cat's reaction to the brown cat finding food?|Is the orange cat interacting with the brown cat or the food?|What is the orange cat's body language or facial expression?|Is the orange cat eating or playing with the food?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The brown cat has found food.")
VIDEO0=CLIP_AFTER(video=VIDEO,frame=FRAME0)
FRAME1=LOC(video=VIDEO0,event="The orange cat is doing something.")
VIDEO1=CLIP_AFTER(video=VIDEO0,frame=FRAME1)
ANSWERS0=VQA(video=VIDEO1,question="What is the orange cat doing?|What is the orange cat's reaction to the brown cat finding food?|Is the orange cat interacting with the brown cat or the food?|What is the orange cat's body language or facial expression?|Is the orange cat eating or playing with the food?")
```

Answer: 2

