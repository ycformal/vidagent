Question: What did the boy do when he first turned to his left after the middle part?

Reference Answer: 2

Video ID: 5031528157

Original program:

```
TIME=FLAG(begin=None,middle="after the [middle] part",end=None)
ANSWER0=LENGTH(video=VIDEO)
ANSWER1=EVAL(expr="{ANSWER0}//2")
VIDEO0=CLIP_AROUND(video=VIDEO,center_frame=ANSWER1)
FRAME0=LOC(video=VIDEO0,event="The boy has turned to his left.")
VIDEO1=CLIP_BEFORE(video=VIDEO0,frame=FRAME0)
ANSWERS0=VQA(video=VIDEO1,question="What did the boy do when he first turned to his left?|What is the boy's body position when he turns to his left?|What is the boy's facial expression when he turns to his left?|What is the boy's mood when he turns to his left?|What is the boy's attention focused on when he turns to his left?")
```
Program:

```
ANSWERS0=VIDQA(video=VIDEO,question="What did the boy do when he first turned to his left after the middle part?")
SELECTED=SELECT(question="What did the boy do when he first turned to his left after the middle part?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA4AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDygW9t/b9va3tqdOVnRZCxJ2bsYfBHTkHA7V2fjmPVvCet6TeXV9Hqs1zaB0kuo1l8vDYKrnII6EH0Nb8vjGy1bX7lV8MaHcQqQZdUlLhGCADOWXLDjHvgVYtviJ4MvtRQeJdGt5IILcQWs/2YyBiW+fCE4ROmO/WsL3djpWmtjMttB0nU/gde601oBqsNy7eanHJlXggcYw3pxUHhnXEvNH0/Sri1tXltbgNGXhLeXHtALdcEluSPau71ex00fCbVJtDtpbOxnVZBGbXyvMO9QDtJJwQOvTHNeW6J5drqarMRteNl57HFEpaWLpwUrs9YvtV0XVZprZpC6RRedIGiITzwNoVsc5AAFec/ELxRaanrNvAkKQpaxgAgHJLKpI+gIOPrWneXzpGj2jkeZhvMyOOAM/TrXB+Iri2bWGd13Fo13EDqQMVpS3IqQS2Kv9oW4ZtrEnPYV9A/DzXJT4a0SJraWWHyVSMxfNgEsCWHbBH5V88KkIJYIuPpXu/g7VbOz+GPh26BdbsSm2UROVL/ADsSrY7dK3lGU7RXUyi4xTbOm8dT2sNtZyxgG788MAi/Myjr+oFdJYaxbaiG8kOCGxhxg1z+uavpWm30d9c2XmO4CNJ94rgbhgE453fpXLaj8VIUurdLOxdreOTc7yyAO55HbgCub2coyNbqpSiktup6pNIiROzuqgKSSSBgYrzfX/Evhe7uNULTx314tn5UEU67YsjPCE9WyQc+3Fcf4r+Ilzr9g1uLSG2t88AHcx/4FXDRRtf6vGrQPJGxOQG2gnBwM9iSKtqyuzONO253gintVWGfXrdHRFGyKbcq/KOMgYP4UVjvdRWaxWs11bwywxhHhjCuIz/dJ9aK5nWd9i7o9auvAOhNbLa3DPJ03Qq4iUg8Z2rjj614H8RdHt9L8b6rYWdssNvCyiKJc7UQoDx+dd/qPi/zbyfUbCKCJj8skodhNIByBg54z7du1eYa/wCKtQ1e5lmkm2xuoQoOcgdiTyeeaqkm3dIjnct2e+Q3UF/8DQzypk6WisM8h1RePrwK8Ju5sNmNgpHQistNauZnhEr71Q4Cn7o/CrEt4ZpyZimWbLNgdzW3s+ppCaUWl1IZdTvchDePtGAqg44qG7glN2VedWOzdvZ8gjGetQ6jKba4wI0ZRxnHeqtrLlzno3XPNa8tiVJN2ZEWbB5NeieC7lvsGnQlmK+czAZ4BDVxF5YG0AHnRTI2CrxtwR9OoPtW7ompR6TpdvePj9zKSqEZ3HPStqM1Cak+hnUi3Fx7nsHji5M+iNcxzpNHDdIhCHd5XylSGGPl6A++a8qupWE0YU/KT3rZ07xjqd74auLW6mK2zRlZCq/NICRwWwTWTLEbsedapm2jj3NhiSvGCCSB1PT/AOtRWkr83QzoScI8rKkkjyIVXbuB5yeB7mo7yNoI9s1yWimALeQ25GI6ZPfGT09at3Wn3VyEks7+EQ4DiLOWQEDjcBgj61iy/u/9GMjlo8oXTJHP/wCvtXE5871NbyZqW2r22nwiIupDfOC8COxB9SSD2ornmiCnCwwkDj5mIP60Vm6aeouQ2ru5MsUhhnjR5MBlA2/KO2f6VjanZNaW6MWJZ2xwOMV6P4G8K2fiC+uLGdlyqcDAbr0wwxjpj865C6WyiMsM9zMVztKsgxx7/WumEGkvMyjLocvGHJHJ5rWvABabVZtysOfUV0WieFV1kTSabazSGH73zKD0z0PXgVnf8SlFAeWfPUA46flW/spFKS2MdGW7k8qeRhHs6r2I6Uye0NttaOYSgY5A6e1egeDfDmia9ePBLHPjICsr4xkfTnpWFEto12kEVnK0hfCgygZIP+77VTpS3fUSlrZGNbwNcQtvVUCj7zHBzV06bcXVlbQRIHiErNuIxyRjOenY8V13hb+z31ZkuraOC3VjveRwyDLDI5HT3qvrWoxLcanpVrBHHEZpEjYNgLhjjGKTotK5ftFJ2Zn2tjrWlmC0vvlS5jYW5MmRgHG7jsPerXh9tag1G7tBOqvC+2Qqwxj14wSOa6a7s0u20KSKSKI+XLuRudwDg1DpVhGmta40U4jKzx4wobIManH0q5Q6IiLs9TNk8MyzzvK8673bc4VOCfpxiq58OzyOzRiJdhK8jAPuOa7WOJ1UiRhNnu3H6Diqt/fJp8avNBIVZtvyDcazdGO5oqrONbRIkdg5uAc9ApIH0orXutb0qSbLQ3pOMHZE2BRUeyQe18xvwwvZbHxbbsZBMskbb33gbmByOOvT+tc/rZhsPF+qqbaOVIb93j3YbGWyBs6Ec96KK05U6UX6mFtfuO0+FN/G+tXMJwocEiMrtK5zXlskCvfS2xYyyQyPGBg5wGOCB3+lFFVJtwg/63Cno2jufhsRZayNwHzsjZA246jBHY1zVwtpa3VzLvYyLcNlgcgLk8EdR9R+VFFObfso/P8AMX2mXNJvY7qaO1LxwxyPuaUj5QAe47iqmorJHq9zMFSVHkd/nHU56rjseo+ooorBSZUUo1FFdTd8Ry/8SfQbjGXVZtrDOQcr6d6raHr89je3kk8c04lMf7w4Vshcd+tFFb7SK6GpceIrmUh7e+liHdJLUHH0bkGnWttLqqJNLrf2jofJRgVX6gYANFFXFXepDdkSNZamjFIp4HQcAlBkfpRRRWnIiOdn/9k=">, <b><span style='color: darkorange;'>question</span></b>='What did the boy do when he first turned to his left after the middle part?')=<b><span style='color: green;'>User: What did the boy do when he first turned to his left after the middle part?
Assistant: He turned to his left, revealing a small table with a black object on it.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=What did the boy do when he first turned to his left after the middle part?, <b><span style='color: darkorange;'>information</span></b>=['User: What did the boy do when he first turned to his left after the middle part?\nAssistant: He turned to his left, revealing a small table with a black object on it.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['feed baby', 'reach for the airconditioners', 'look at camera', 'stretch out his hands', 'sit down'])=<b><span style='color: green;'>3</span></b></div><hr>

Answer: 3

