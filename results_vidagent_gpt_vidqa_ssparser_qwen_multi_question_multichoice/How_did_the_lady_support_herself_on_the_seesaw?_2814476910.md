Question: How did the lady support herself on the seesaw?

Reference Answer: 1

Video ID: 2814476910

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How did the lady support herself on the seesaw?|What is the lady doing?|What surrounds the lady?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How did the lady support herself on the seesaw?|What is the lady doing?|What surrounds the lady?")
SELECTED=SELECT(question="How did the lady support herself on the seesaw?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDFGi3dwxWJOMZY85/lStoMymNWjjJ64AJP45Ga9KhgVUYuwYnqBxz7GomjV22RxogB+8zA7vwHNT7MV0edjw9eyAubeJV7EMoz+fWozpN0zAxxHeDjOCoH9K9Lmt4o13FZXP8ACDhR+OTRHAVcSb05/hRfu+1HIF0ecf2LeQBgyDGcsY2DE/rT30DVChK258teSDIAf58V6F5KszL5caejud/14NOjsk2Yc7UXn5eho5AujztNFvpvlSDBQ4AWQbQPzqOXw/qNqxkliAU/xlh+gz0r0dolmkBEiqo7MoLN+VSSQQqc8GQ8/vcUezC6PNRoeoSrtt4JWAGTj+L6Ur6XfbdrW0hdRkIpLNx616NbW3zOZgpD9TGf5nHSmGPI2RlFQcE7vmP6UezDQ86Hh7UN3nvaOqkZGUOPxwKb/ZN5KdsUbSMTwTyAPpivTGgiRVG5c448xfl/AdqZFC7sWLIzsf8Aln0x7elHIF0eeDw3chRxEpPJDbs5/wC+aK9BeK3V2EkQ3Z/v5oo9kF0XWRWISFmSMdRkY/lSNbWqfO0m5u+4ZzWFLdvEqgfO56hARxSRXU/LlljH+02a2M7m8YVnx5sgWLsoH/16BFHEdsEnXruHT8awJL+bdiNWb3IGKeb54ofvfMf4VHP40ahc3ha2obfIzOx6ndTGhMqmNJxHEDnlBk/rXPpezyyeij1kIzSyX7xLsjeRj14OFH0oC50Iht4VxHzIT1zjP4U37GhO+affn+HGf1rCS5lZN8pPHII65qL7bM8u0AAerH/69GoXOjMa4MUMjBT1Y4pptbdDv89nkHHJH9BWG988aAI245/hPA/GhLy6J3O+xfc0ahc3vs4kffLJheyg84pWjgj+W23q57gjArnm1KaSRljIYZxliBTpLl4UyTuY+gP86Aub628QHzyEt67qK5s3twT8vA95KKLMLmG1w7KWWT5R1z1pBdFs4kPPGSRXOC4SFBJNKS46Lmk+23EzAmTaG75o5idTozcPtx5+CPQkfrmnNO+FJkYADq3Nc19rEDMsbB3I5Of50kdyHy9zKeDwBz/+ujm0HqdL9ofd/rGYc5+bj8qGuHAIabbg9D2rmjqEsuPLciPsCe1OFzHA43F2fGeSP60cwanR/aW2gpKwzk/Men50NdNuH712B7g8fnXNLPJICZnKoOcBj+pFBv3MIS3BXsQecfjRzahqdIbkkHDhQO3ekW5+b/WMG65PFc4s6ooeeRt57EZpTdT3DHEhEfbB7UcwtTozdMxwZfY7T/hSm5kChUbgep/xNc39uEaBLYuZCSW3D+uabHNklrmZgvYZzzRzBqdF9pJ/5emX2wDRXPDVJQMI0e0dOGNFPmHZmbhCS7zx5P8AtKcfrT2uVK7I5IF/2jKgz+GaR9ZuYjgTYbPoOP0qMajeuMtfXA9AJKyuzTlRLE1vG7EyozE5wXUj8801iHGZJk4PAVgRig6jcxp81zcMR38xv8ari9nlJb7XcL6nz5Bn9aLsOVF0bvKBiZd3qe1CQ/MHdXOB94I1U/MbGXmnkBPed/6mq5dZGPDKPXcen50Bymq8Mshzsfb2Cox/PipFt5EjLLDITjjMT4/lWQIIt2WG5R/eOaC1uXCpbQ5A7xg5/MGncOU1DbSzOGdX7cCNsD9KJN7ZQI6j+9jn6dKz1WJWUtb24HXmBMfTlaDeIpzFaWvoSLaM/wBKVw5S2I1jRWOS3pkf1oYiX78kYx2Lrx+tQR3Ei52+UOe1vGB/KpW1eaJRGvkkYxgRJ/LFF2HKhyywoMF4m9yyj+tFMGr3/a5dR6DGB+lFL3g5UUjHlstvPrnB/GlJ28IMsenO2oXdth575oEjF9pOR7imUSqjlfmJIPIGSf604MII/l6n1pwRdp+UcDPSkCjHU/maAIVXf8xJPPZQalUBTu3c9x0ph5UEknk96tQopCnAyaAKjnzX6qAOODk1IiKMEsePXNWzCmTwevqageNfn47etAEMhZztJAX35pgRFA5yO/FWERcNx0Ap0gC9OOKAGAsFwowPUsKjMYVgWLeuRzSElsbiTnrzTo1XrjPPegBFKgcMMe45opc5J4Xr/dFFUgP/2Q==">, <b><span style='color: darkorange;'>question</span></b>='How did the lady support herself on the seesaw?|What is the lady doing?|What surrounds the lady?')=<b><span style='color: green;'>User: How did the lady support herself on the seesaw?
Assistant: hold ski stick

User: What is the lady doing?
Assistant: The lady is walking.

User: What surrounds the lady?
Assistant: The lady is surrounded by a lush green landscape.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How did the lady support herself on the seesaw?, <b><span style='color: darkorange;'>information</span></b>=['User: How did the lady support herself on the seesaw?\nAssistant: hold ski stick\n\nUser: What is the lady doing?\nAssistant: The lady is walking.\n\nUser: What surrounds the lady?\nAssistant: The lady is surrounded by a lush green landscape.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['hold ski stick', 'legs on the floor', 'wear life jacket', 'hold up cup', 'from her hand'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

