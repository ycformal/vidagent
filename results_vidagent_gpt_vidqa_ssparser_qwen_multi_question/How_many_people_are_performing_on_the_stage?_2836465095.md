Question: How many people are performing on the stage?

Reference Answer: 2

Video ID: 2836465095

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people are performing on the stage?|How many performers are on stage?|What is the number of people on stage?|How many individuals are participating in the performance?|What is the size of the group on stage?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people are performing on the stage?|How many performers are on stage?|What is the number of people on stage?|How many individuals are participating in the performance?|What is the size of the group on stage?")
SELECTED=SELECT(question="How many people are performing on the stage?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwESOBjc350eY/99vzptFADvMf++350eY/95vzptFADvMf++350eY/99vzptFADvMf++350eY/99vzptFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFBOaKACiiigAooooAKKKKACiiigA7UUUUAKAPUUUlFABRxRRQAUUUUAFFFFABRRRQAY4zRRRQAUUUUAFFFFAH//Z">, <b><span style='color: darkorange;'>question</span></b>='How many people are performing on the stage?|How many performers are on stage?|What is the number of people on stage?|How many individuals are participating in the performance?|What is the size of the group on stage?')=<b><span style='color: green;'>User: How many people are performing on the stage?
Assistant: There are two people performing on the stage.

User: How many performers are on stage?
Assistant: There are two performers on stage.

User: What is the number of people on stage?
Assistant: There are 10 people on stage.

User: How many individuals are participating in the performance?
Assistant: The exact number of individuals is not specified in the description.

User: What is the size of the group on stage?
Assistant: The group on stage is large.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are performing on the stage?, <b><span style='color: darkorange;'>information</span></b>=['User: How many people are performing on the stage?\nAssistant: There are two people performing on the stage.\n\nUser: How many performers are on stage?\nAssistant: There are two performers on stage.\n\nUser: What is the number of people on stage?\nAssistant: There are 10 people on stage.\n\nUser: How many individuals are participating in the performance?\nAssistant: The exact number of individuals is not specified in the description.\n\nUser: What is the size of the group on stage?\nAssistant: The group on stage is large.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['four', 'nine', 'two', 'six', 'five'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

