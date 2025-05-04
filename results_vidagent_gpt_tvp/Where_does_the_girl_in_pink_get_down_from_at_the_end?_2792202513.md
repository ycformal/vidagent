Question: Where does the girl in pink get down from at the end?

Reference Answer: 1

Video ID: 2792202513

Program:

```
ANSWER0=LENGTH(video=VIDEO)
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER0)
FRAME0=LOC(video=VIDEO0,event="The girl in pink is getting down.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="Where is the girl in pink getting down from?")
ANSWER0=SELECT(question="Where does the girl in pink get down from at the end?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: Failed to extract frame at 13.396949780923492 seconds.

