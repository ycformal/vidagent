Question: What is the color of the child s shirt who is standing?

Reference Answer: 2

Video ID: 11794871936

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="A child is standing.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the color of the child's shirt?|What is the child wearing?|What is the child's posture while standing?|Is the child facing the camera or turned away?|What is the child's expression?|Is the child interacting with anyone or anything?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="A child is standing.")
VIDEO0=CLIP(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the color of the child's shirt?|What is the child wearing?|What is the child's posture while standing?|Is the child facing the camera or turned away?|What is the child's expression?|Is the child interacting with anyone or anything?")
```

Answer: 2

