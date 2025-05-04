Question: How many people are there?

Reference Answer: 0

Video ID: 5589529025

Program:

```
ANSWERS0=VQA(video=VIDEO,question="How many people are there?")
ANSWER0=SELECT(question="How many people are there?",information=ANSWERS0,choices=CHOICES)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA4AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwiim5pM5NAEt1KzrGrHIRcCololGDjOaRabAeeg+tKzfLikPb60jdDSAuWEnmymKQAjbwfStn+zoZLYhVG72rn7LP2yP0JxXRW7NbyJGwOw8A1lPfQ1g09CHTbZY5mR15HStrTT9lstSTLP5kLcMehyMflVZkAk3qOT3p2RtOc88HnrWd7m8dBYCD97vV/wCxxTLyoIrJaTaeDViPUGRMZovYllw2Yj+VeB7UVzt14gnNw3lgFRxknrRVcsieaJz2xvagI3qKduo3Vuc4rq8jbnfJpoGKduppNABxxQeQfrRxx9aRs9B60AS2rYuYwPWullk2QJIwyp68ZwRWl4b8BS+dDe6w6RxcMtuOWbPZvT6Vf8QWcUDo1rCqRbdpRRgAg81lLe5pTV5GGlyrxq3YjPNNecY4NW9NtobuXyblXCtwGUgFSeh5qnqmlXenNOJEJSI8t7djUqJs9ClPchTkmqE1082V3lV9B3qq0jMxLcmlV1PqK0UUjGUmx20UU7iiqIKeaM02imIdmjNNpaAFHWu/8D+G4JYxrF9EJBvP2eNhxkfxn156VzPhfQm8Q61HabtsK/PKc4O0dh7mvbI9NjtLaNUiAtY1CBV6x46UWb0QFVxI7BmPBqveeH7mfHyrw5JyezdOa30giEboxDx7d2R1A9a0dOvrf7JPbNIrTQ7SQw/hPb8M/rWsaCe4nO2xwsXwuk1GbzJpPLTpnO41S+Ivh+x8KeErS0gd5bm6uQGkc9FVc4A7DJFenw3ce/bCPwWvMPjXcO93o0LYwsUj4+rAf0rWVOEINpB7STdm9DyoihlwAR1oI6U49K5ShquMcnBoqOigCHNFFFAgqWCGW5nSCFGeWRgqqoySaKKAPbPDHgd7PTo0aJopfvmVTh93r/8AWrro5WtiltftGJ2GFl24SUehHY+35UUVvTgo6oJSvoZ3iKW30TSWvxlWX90ITyJCTwAf8e1cLbX15cyFzNskkJLbTtJJOe9FFXV0dkRDVXOs0ZdWiwFQFT3Y5z+tcj8XI5xeaVNOy7mhdAB2wwP9aKKJL92wXxHnJ6Uh+6aKK5TQiooooA//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many people are there?')=<b><span style='color: green;'>['2', '2', '3', 'two', '2', '3', '3', '4', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '1', '2', '2', '3', '2']</span></b></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are there?, <b><span style='color: darkorange;'>information</span></b>=['2', '2', '3', 'two', '2', '3', '3', '4', '3', '3', '3', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '1', '2', '2', '3', '2'], <b><span style='color: darkorange;'>choices</span></b>=['three', 'six', 'four', 'two', 'five'])=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>3</span></b></div><hr>

Answer: 3

