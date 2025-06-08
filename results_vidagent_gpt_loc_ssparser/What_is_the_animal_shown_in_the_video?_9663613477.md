Question: What is the animal shown in the video?

Reference Answer: 1

Video ID: 9663613477

Original program:

```
ANSWERS0=VQA(video=VIDEO,question="What animal is shown in the video?")
```
Program:

```
ANSWERS0=VQA(video=VIDEO,question="What animal is shown in the video?")
SELECTED=SELECT(question="What is the animal shown in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What animal is shown in the video?')=<b><span style='color: green;'>['The video shows a small dog, likely a Chihuahua, based on its size and physical features.', 'A dog.', 'A dog.', 'A dog.', 'A cat.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'Dog', 'Dog', 'A dog.', 'The video is too blurry to determine the exact species of the animal.', 'A chicken.', 'A snake.', 'A dog.', 'A dog.']</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What is the animal shown in the video?, <b><span style='color: darkorange;'>information</span></b>=['The video shows a small dog, likely a Chihuahua, based on its size and physical features.', 'A dog.', 'A dog.', 'A dog.', 'A cat.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'A dog.', 'Dog', 'Dog', 'A dog.', 'The video is too blurry to determine the exact species of the animal.', 'A chicken.', 'A snake.', 'A dog.', 'A dog.'], <b><span style='color: darkorange;'>choices</span></b>=['birds', 'dog', 'squirrel', 'rabbit', 'elephants'])=<b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

