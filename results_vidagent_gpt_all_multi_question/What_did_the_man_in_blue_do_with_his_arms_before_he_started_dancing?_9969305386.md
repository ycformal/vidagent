Question: What did the man in blue do with his arms before he started dancing?

Reference Answer: 1

Video ID: 9969305386

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man in blue has started dancing.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man in blue doing with his arms?|What is the man's body position before dancing?|Is the man interacting with anyone before dancing?|What is the man's facial expression before dancing?|What is the man's mood before dancing?|Are there any objects or props involved?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
FRAME0=LOC(video=VIDEO,event="The man in blue has started dancing.")
VIDEO0=CLIP_BEFORE(video=VIDEO,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO0,question="What is the man in blue doing with his arms?|What is the man's body position before dancing?|Is the man interacting with anyone before dancing?|What is the man's facial expression before dancing?|What is the man's mood before dancing?|Are there any objects or props involved?")
```

Answer: 1

