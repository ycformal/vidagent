Question: Where is this happening?

Reference Answer: 2

Video ID: 2406887888

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this happening?|Where is the location of this event?|Where is the setting of this video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this happening?|Where is the location of this event?|Where is the setting of this video?")
SELECTED=SELECT(question="Where is this happening?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwQTMGztjP1UU77UwORHD/AN+1pouZgciVgfXNP+3XR/5eJP8Avo0ANNy5GNkX/fpf8KaZWJyVT/vkU77VP/z2f86T7TNnPmvn60AKtyyjhIfxjU/0pTdOTnZCP+2S/wCFKb67PW5lP/AjTftdxjHnSf8AfVAA1wzdUi/CNR/SnC7kChdsRA7GMGozcTHrK5/4FThd3I6Ty/8AfZoAUzyMf9VF+EQH9Kb5rf8APNP++BSm8uicm5mJ/wB80huJ+80n/fRoActyyggRw8+sYNIbhzz5cXH/AEyX/Cmi4mHSVx/wI043l0Rg3MxHu5oAPOf/AJ5x/wDfsf4UUovLoDAuZv8Avs0UAQUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFKccYFJQAUUUUAFFFFABRRRQBJuj/wCef/j1Nyufun6ZppOaKAF+X0P50vy+h/Om0UAOyn91vzo+TH3Tn602igBfl9D+dHy+hpKKAF+XHQ/nR8vvSUUALxjvmkoooAcu3HI/Wim0UAP3L/zzH5mgsn/PMD8TTKKAFyv939aX5fT9abRQAuV/u/rRlf7v60lFADsr/dP50hI7L+tJRQAvbODRx6UlFAC8en60cen60lFADw6gfcB+tFMooA//2Q==">, <b><span style='color: darkorange;'>question</span></b>='Where is this happening?|Where is the location of this event?|Where is the setting of this video?')=<b><span style='color: green;'>User: Where is this happening?
Assistant: on the road.

User: Where is the location of this event?
Assistant: The location of this event is the beach.

User: Where is the setting of this video?
Assistant: The setting of the video is a beach.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this happening?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this happening?\nAssistant: on the road.\n\nUser: Where is the location of this event?\nAssistant: The location of this event is the beach.\n\nUser: Where is the setting of this video?\nAssistant: The setting of the video is a beach.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['swimming pool', 'garden', 'living room', 'trail', 'on the road'])=<b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

