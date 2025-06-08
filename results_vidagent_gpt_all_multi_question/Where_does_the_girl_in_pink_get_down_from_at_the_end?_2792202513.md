Question: Where does the girl in pink get down from at the end?

Reference Answer: 1

Video ID: 2792202513

Original program:

```
TIME=FLAG(begin=None,middle=None,end="at the [end]")
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The girl in pink is getting down.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="Where does the girl in pink get down from?|What is the girl in pink doing before getting down?|What is the girl's body position while getting down?|Is the girl assisted by anyone or anything while getting down?|What is the girl's facial expression while getting down?|What is the girl's mood or intention while getting down?")
```

Program:

```
TIME=FLAG(begin=None,middle=None,end="at the [end]")
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The girl in pink is getting down.")
VIDEO1=CLIP(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="Where does the girl in pink get down from?|What is the girl in pink doing before getting down?|What is the girl's body position while getting down?|Is the girl assisted by anyone or anything while getting down?|What is the girl's facial expression while getting down?|What is the girl's mood or intention while getting down?")
```

Answer: 0

