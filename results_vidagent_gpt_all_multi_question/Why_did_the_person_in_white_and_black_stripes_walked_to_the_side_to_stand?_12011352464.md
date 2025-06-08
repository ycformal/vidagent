Question: Why did the person in white and black stripes walked to the side to stand?

Reference Answer: 2

Video ID: 12011352464

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The person in white and black stripes has walked to the side to stand.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Why did the person in white and black stripes walk to the side to stand?|What is the person doing before walking to the side?|What is the person's body position before walking to the side?|Is the person interacting with anyone before walking to the side?|What is the person's facial expression before walking to the side?|What is the context of the person's movement?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The person in white and black stripes has walked to the side to stand.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="Why did the person in white and black stripes walk to the side to stand?|What is the person doing before walking to the side?|What is the person's body position before walking to the side?|Is the person interacting with anyone before walking to the side?|What is the person's facial expression before walking to the side?|What is the context of the person's movement?")
```

Answer: 3

