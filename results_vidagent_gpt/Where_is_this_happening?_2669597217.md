Question: Where is this happening?

Reference Answer: 1

Video ID: 2669597217

Program:

```
ANSWERS0=VQA(video=VIDEO,question="Where is this happening?")
ANSWER0=SELECT(question="Where is this happening?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDgFdtoG5unrRuYnJY5+tNH3R9KWgBdzf3j+dG5v7x/OkooAXc394/nRub+8fzpKKAF3N/eP50bm/vH86SigBdx9T+dG5v7x/OkooAXc394/nRub+8fzpKKAJo3bafmbr60U2P7p+tFYS3GRD7o+lLSD7o+lLW4gooooAKKKKACiiigAooooAKKKKAJI/un60UR/dP1orGW4yIfdH0paQfdH0pa2EFFFFABRRRQAUUUUAFFFFABRRRQBJH90/WiiP7p+tFYy3GRD7o+lLSD7o+lLWwgooooAKKKKACiiigAooooAKKKKAJI/un60UR/dP1orGW4yIfdH0paQfdH0pa2EFFFFABRRRQAUUUUAFFFFABRRRQBJH90/WiiP7p+tFYy3Gf/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Where is this happening?')=<b><span style='color: green;'>['in bedroom', 'in bedroom', 'in kitchen', 'in computer', 'tennis court', 'tennis court', 'in living room', 'in snow', 'tennis court', 'outside', 'ocean']</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this happening?, <b><span style='color: darkorange;'>information</span></b>=['in bedroom', 'in bedroom', 'in kitchen', 'in computer', 'tennis court', 'tennis court', 'in living room', 'in snow', 'tennis court', 'outside', 'ocean'], <b><span style='color: darkorange;'>choices</span></b>=['play an', 'boat', 'wooded areas', 'hospital', 'outdoors'])=<b><span style='color: green;'>4</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>4</span></b></div><hr>

Answer: 4

