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

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDgA7YHzN09aN7f3m/Omj7o+lLQAu5v7x/Oje395vzpKKAF3t/eb86N7f3m/OkooAKKKKACiiigAooooAkj+6frRRH90/WisZbjIh90fSlpB90fSlrYQUUUUAFFFFABRRRQAUUUUAFFFFAEkf3T9aKI/un60VjLcZEPuj6UtIPuj6UtbCCiiigAooooAKKKKACiiigAooooAkj+6frRRH90/WisZbjIh90fSlpB90fSlrYQUUUUAFFFFABRRRQAUUUUAFFFFAEkf3T9aKI/un60VjLcZGPuj6UUg6D6UtbMQUUUUAFFFFABRRRQAUUUUAFFFFAEkf3T9aKI/un60VjLcZ//2Q==">, <b><span style='color: darkorange;'>question</span></b>='How many people are performing on the stage?|How many performers are on stage?|What is the number of people on stage?|How many individuals are participating in the performance?|What is the size of the group on stage?')=<b><span style='color: green;'>User: How many people are performing on the stage?
Assistant: There are two people performing on the stage.

User: How many performers are on stage?
Assistant: There are two performers on stage.

User: What is the number of people on stage?
Assistant: There are 10 people on stage.

User: How many individuals are participating in the performance?
Assistant: There are 10 individuals participating in the performance.

User: What is the size of the group on stage?
Assistant: The group on stage is small, consisting of a few individuals.

Note: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are performing on the stage?, <b><span style='color: darkorange;'>information</span></b>=['User: How many people are performing on the stage?\nAssistant: There are two people performing on the stage.\n\nUser: How many performers are on stage?\nAssistant: There are two performers on stage.\n\nUser: What is the number of people on stage?\nAssistant: There are 10 people on stage.\n\nUser: How many individuals are participating in the performance?\nAssistant: There are 10 individuals participating in the performance.\n\nUser: What is the size of the group on stage?\nAssistant: The group on stage is small, consisting of a few individuals.\n\nNote: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.'], <b><span style='color: darkorange;'>choices</span></b>=['four', 'nine', 'two', 'six', 'five'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

