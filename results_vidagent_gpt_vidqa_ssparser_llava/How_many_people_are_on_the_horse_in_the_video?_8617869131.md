Question: How many people are on the horse in the video?

Reference Answer: 3

Video ID: 8617869131

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people are on the horse?|How many people are riding the horse?|How many people are interacting with the horse?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people are on the horse?|How many people are riding the horse?|How many people are interacting with the horse?")
SELECTED=SELECT(question="How many people are on the horse in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>question</span></b>='How many people are on the horse?|How many people are riding the horse?|How many people are interacting with the horse?')=<b><span style='color: green;'>USER: 
How many people are on the horse in the video?
Choices (choose one): eight, five, four, one, two ASSISTANT: There are two people on the horse in the video.
USER: 
How many people are riding the horse? ASSISTANT: There are two people riding the horse in the image.
USER: 
How many people are interacting with the horse? ASSISTANT: There are two people interacting with the horse in the image. One person is riding the horse, and the other person is leading it.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are on the horse in the video?, <b><span style='color: darkorange;'>information</span></b>=['USER: \nHow many people are on the horse in the video?\nChoices (choose one): eight, five, four, one, two ASSISTANT: There are two people on the horse in the video.\nUSER: \nHow many people are riding the horse? ASSISTANT: There are two people riding the horse in the image.\nUSER: \nHow many people are interacting with the horse? ASSISTANT: There are two people interacting with the horse in the image. One person is riding the horse, and the other person is leading it.'], <b><span style='color: darkorange;'>choices</span></b>=['eight', 'five', 'four', 'one', 'two'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

