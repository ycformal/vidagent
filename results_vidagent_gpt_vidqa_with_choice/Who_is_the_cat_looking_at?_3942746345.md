Question: Who is the cat looking at?

Reference Answer: 4

Video ID: 3942746345

Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="Who is the cat looking at?")
ANSWER0=SELECT(question="Who is the cat looking at?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAEsDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD5/ooooAKKKKANDRU8zVYfYk/pVe9k82/mc9DIfyzTbaaSCbfE5RsYyKiOSxz1pdR9Da0AB7sZ7tmurxXJaHcw20pMzhAPXvW8dasR/wAtvyU1hUu2NLQuEVyt/dSNfTFG+XdgfhxW0+t2e3h2z/umuWcgyMQSeTyeM06a7iZVooorcQUUUUAKvWl/ipB1pe9IY9etP3UwGkJqbDJQ2e9HWos0uTRYLkVFFFWSFKKSlUFjgUDQvSg4q1b2byglVz7npTmsZBknGBUcyL5XYpg0u6rC20ZIy/4CpzYIR8vHuaHJAoSexnlqTNW5LAqMq+RUHkP6U00yWmtyKiiiqJHRxtLIqIMsxwBXQW2kCOH5sFj1NVNChDTPKRnbgCtme4ISQL1CmuepJ3sjenFWuyJYkigwnAHSiztPt1z5O/Zxk1DFIZYx9KkWc2lwkq/w9az1KbItY01dMukKDfGw6Z71lSPO5JztB7Zq/f6l9uneV+mcAVXWaM9q0jtqJ7EMRmz85yop5PNT8FeKiMYJzmqTJZlUUUVsYmvpcvlWj+7/ANKsNK28+hrLs5du5CeDzVwOcVhKPvG0ZaEkM4hk8thx2NOvJQVyKpTEHHPNV3kYLjdwKaiJsDLsyrDOTmgPEcZ61ASSck5NJWnKRzsvLLtHByKf52e4rPBI6U7fS5R8wyiiirIFVirAirYmx1qnTgflqWrjTJpJs9KizmmUo6U7WC4hooopiCiiigAooooAKUdDRRQAlHaiigAooooAKKKKAP/Z">, <b><span style='color: darkorange;'>question</span></b>='Who is the cat looking at?')=<b><span style='color: green;'>The cat is looking at the person feeding it.</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Who is the cat looking at?, <b><span style='color: darkorange;'>information</span></b>=['The cat is looking at the person feeding it.'], <b><span style='color: darkorange;'>choices</span></b>=['his parents', 'the baby', 'stranger', 'deaf people since have sign language', 'adult'])=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

