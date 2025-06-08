Question: How many people are in the video?

Reference Answer: 3

Video ID: 5969368435

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How many people are there?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How many people are there?")
SELECTED=SELECT(question="How many people are in the video?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA4AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDnM4BPpTlbIBwRkd6iPKMPUGkgP+jx/wC4P5UhFjNNMqK6oXUO2dqk8nHXFJmuP1C6vJpobhJSqiVlhIPIPGf5jimOx2ec1FNIY0BVC7FgoX3JxTrCO5urOGUxHey/N2GRwf1FWW067dDs2o45Ulu/4UgW5iaVqct3cXME6BZI2yBjBxnp+Famaq6b4ZvLO8kuJriGR5SQxAP1yPxraGlHHMv5LQDRn5orTXTYcHLPmnjT7dRyGY+5piMnNIa1/sNv/cP5mgWkK/8ALNSPekIxqK2fssB5MSflRQBUXSv7035LUsOmQRxquXfAxycVeFIDnhfzpjIltoU+7Ev5Vk6tZy386QRwLtEMigkcKzYANbgGNxJJqG2CL8qKwHuScfiaBkkMTRxqGI4HYVKCKVlVlKsMj0pjKFkQb8ccJxzQA89RxwOabuLKGA4PTNOYNztxkcj3+tMDYIVvvE5IJ6UAKo2jnqP1p2c1T84MJQucxk5Xrk1ZjdnRXZSmeqmgBc/e4qIE4OBk+nSpzxzUEgBBzjGO9AiJ5EjbDY9RmiphnAzwaKQh3UelLgIKUCgRgkZz1zwetAxgQrHhSzHHG5uaSCExKFVUUZztX3qVS245XHPHNKoyWOMdvrQMdj3pjA793pUnNQbizk7W646UwCCV5HbMbqB3cYJpu799GoyNykgY/OpYVYOxLE+gxT8FjuOR7UAQg/M2EyR6CnjpyeT0BpwXaMU0fM2SpBXpmgBoYnIxyKjKl0ZXXbnjINTHAOfWo2ODmgRHEkiRhZJd7D+LbjNFO3UUASinUUUhig5pc4oooAGb5TjmoDJIR8qc0UUASxFiPmGDUlFFADT7U38aKKAEIJqF0f8Ahb86KKBEXlyCiiigD//Z">, <b><span style='color: darkorange;'>question</span></b>='How many people are there?')=<b><span style='color: green;'>User: How many people are in the video?
Assistant: three.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How many people are in the video?, <b><span style='color: darkorange;'>information</span></b>=['User: How many people are in the video?\nAssistant: three.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['seven', 'two', 'three', 'five', 'eight'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

