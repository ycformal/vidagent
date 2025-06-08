Question: Where is this video taken?

Reference Answer: 3

Video ID: 7526364640

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where does the action in the video take place?|What is the background of the video?|What landmarks or objects can be seen in the video?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where does the action in the video take place?|What is the background of the video?|What landmarks or objects can be seen in the video?")
SELECTED=SELECT(question="Where is this video taken?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0q3DS+GoOSRtG0n3VxXkU6GO1hB4KSQH8VkX/ABr2OxWQeG7ReMbUPHT72P614/qJwblefkcj9c/+y1hjFqmd+A1hJHuEY3C1PX7w/lWkIQSDisuFs21i3qT0+lbyD5BWkNUc0pWOaWItZkjtI4/8eNU2Xa4G08djWxaJts2z/wA95Of+BGo7hAzdAB6Vxez91HSpmRMCkZI9RUJk4C1heMfHui+FilteNJNdP83kQ4yB/tHtmub0v4paXrOopAY2td52gSHI56cj3rmdF2bK51ex2EspMpHXNZ8jZI+uKtSkE+gNZ0jjePrXO42NGPuFCKSGzntUSkBO/Iptw5JXnjFMLZ71FgHZA60VCXOaKdhFbRPGWtXd1Z28z3D2gmHmuseI1Uc4OBgc4rO1sKL+/K9GYsPzJ/rXpdrpSp4R1O4zIWlgfBZieM56YHSvKvE8v2LVxbyht8mAP94EcGvZqxklrqRhqynFy5bHtdjL5mk6e4PVv6V06fcH0ritMuA2h2TDoHX/ANBrsbZ98CnPatqesTjqGbaDfbzKT0nkH/jxrG8T6tDoGh32pXDKot42YZONzdgPcnFbViMRXXtcyfzrgPilLpr6ZbW+pX0EMbTEtE7/ADMCrKGC9TgkGsre4apnzrML/wASX8twEaWSRizzSsTkn1NJc+H76wgFwkilk5ISuvSKTT9OihtIEk2gAgnafrVK7mnMhhNvuAHzMG4Wud1pJ2jsX7NNXe53PgPxA+teHENw+6e2IicnqR2P5fyrYmYLLnPGeK4b4fwRQWt9KtxHFGXCgsThm6n8q6aS6DlWVw4B6joa5a/LzNI1g24q5fZyXGPSkZsR7u9VzcAyc9hiiSXMfWsIq6KJfM+lFVd4oq+UD0jxJ4ij0zTxZGElLhHRSoLHt+GD0yTx715Z42gj1BIdTiD71uI3JxwAxweRx1P6UzW/FXifxXoMl4NOVrWzGZTbw/KitxjrntmuQt73UL+5igupWtLDnc4IXaBwpCHryP5131VU5+dy93sctJezjydT3LRLvztCt/Xcjfoc/rXdac58peeMV5Bo+vwxo1mI2XZN5kUjsADGeRn0PPTtXoUni3RtJsPOvtRgiRFyQH3E+wA6n6V04epGSsmRUT3ZBrniW28M6Hql/cSogW7aNA5wC5xgf1/CvmvXdau9c8dW17A6X0w2sMncrYJJB9hXW/EDxvpvjXSbrSdIWV3Fy18pYYJCjBXb64JPXtXI+CLM2epSy3cTRStAWiLjACfxMfTtVL3Y6kSd3oaC3DXVlbXM8/76WITOTwCxJ/Tis+SSSV55ZZAwCFnEZwCAKfcPaR2ltJBIZbZpJIlI4ATcWX+Zq82nJctDp9qjsLjabmYjiNBglR7npXNKn77NlUtAz49UsdAtYrJnmninAkbynAeE/wBc56H0rqdNv4rhIvIcGLaMf5PNcPZW2lRazei4dQ6TMsMUg4xnr7mrumXDQa3qcUWW+ZXVRzzkZpYijHk5upNOo1Kx6F5wZz0qQyKUGDg4rB0++kmfEqYbBJwenXrV8yN5eUG49h6mvOXu7nZe5fByAaKy4NTiePdIyRHJAUsCcZ60VrZCujC+IOpajoGoReH7W58q0tV3jyW+WR2P3j6nAXHoOKyLnVfNtoNQcpJ5cuIw6hpH+X9OQfwNXPEbW3irVbe/ScFtm26J4OckjH59fzrL1nQrPTNPs7601B7kBtksTx4Ck5IKnuOxr1VTUtUtjiblG6Z10a65d6bLr9po81rpKRmRZ5DlflHGPbIxmuL0fV5r3X0k1G4Zon3GYseGGD8pHTB6cV1dhr9/ffDmfQpvMhtjE/2SUciQbwWXHYZIH41xFho9wL5GkkSERsGL8Ngg9Md6ypQpwT5TRQq1bWVzqI/DmrWOqi98qzhWAjeIpBuUAYOB3qrdXc+qXN/aMVMjWj+XjglgVbH4gGvUb640fU9BS7SVGvQg2KqBTjIBBx29jXluq2qRa1A0TrATKoMh4C5PU+1a1a9Gc4ummu/r5EfV6lNONTcxdGM1xbTWxjd4I2E5Kj7u3kj8RU+n+J5oPEMd7ISLcna8YPAQn+fetmMlbYz6eUuI/tT2skYwuG5IkX1BHOO1ZEtitjq6XEtnIwbDIi4I3k8Z9q1aTVzDyMrVvNm1e6kK53zMAVHB54/pXSwaemng3K/K0dviQ578c/XNaegiOe6uYdVh3RFlmjGD8rjvn6Vb1ma2eI2kMAWJ+HyOtc1WpHl5Wawg27lDSb1TBdzs6kRIM4PJyegHc1NdaysmkTPEr7AwVyPvLkHr7daz307TrGwa/RT9og+YoeQw7bfQ5x+Fc9H4l1RHX96rosZiEbxgqFJLEY+pJz1rJYajUpKUHd39LWKVdqVnsacEjyx7hMAucLuTt+VFYG+ViWcuCT0VsAUVr9UT1uh+08jehkitoQkbeZdOCG2849ABV7RbLT9ZiNrqUtypiIkSOLA39uSfuj3rK8Ij/ipoT33EZ78nB/Qmom1C7iuJIo53VHchgO4ya6ZQa92+xnDSN5anX3dwl1p0QtLKO0hVCEKH5GC4UgZJ9M9uRmsKbT79bfzDC4iYZU56j2qnY3U40oRCQ7FMgA9OQa9AsYY54II5Fyojl46dMYrndKMV7qsdFLEzhGyKvhe0dZLkXPyIIC0Ubr8yseOvpj86o3z21tqMklzDFIgt5MCUAjdjj8a0NNdvLumychwo+nNZXjKJI7qy2DHmRnfznPAqeRe6/M1qVHKzkcXb6n5FikagR3NvN50Uir97PBVvX2/EVd1nU7rUNNt52hMcTNgsOmV//X+lYDfeNSvPL5CRea/l4+7u4rsPNOs8OamJXgF5evJcFjHFF6DHU+v41p6ySkDyLwQMg1w+kErq9mQcHzl/nXfayimx6d64MTFKSZ1UX7rRh6lMxspOhVlZSQenHU1yZ+Q4710OqEvps5Y52uMfnXOGtsNC1M573DcfU0UlFdArn//Z">, <b><span style='color: darkorange;'>question</span></b>='Where is this video taken?|What is the location of the video?|What is the setting of the video?|Where does the action in the video take place?|What is the background of the video?|What landmarks or objects can be seen in the video?')=<b><span style='color: green;'>User: Where is this video taken?
Assistant: The video is taken in a cozy room with wooden walls and a large window adorned with pink curtains.

User: What is the location of the video?
Assistant: The video takes place in a cozy room with wooden walls and a large window adorned with pink curtains.

User: What is the setting of the video?
Assistant: The video is set in a cozy room with wooden walls and a large window adorned with pink curtains.

User: Where does the action in the video take place?
Assistant: The action takes place in a cozy room with wooden walls and a large window adorned with pink curtains.

User: What is the background of the video?
Assistant: The background features a wooden wall and a window with pink curtains, allowing natural light to fill the room.

User: What landmarks or objects can be seen in the video?
Assistant: The video shows a wooden wall, a window with pink curtains, and various props like crowns and a black case.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Where is this video taken?, <b><span style='color: darkorange;'>information</span></b>=['User: Where is this video taken?\nAssistant: The video is taken in a cozy room with wooden walls and a large window adorned with pink curtains.\n\nUser: What is the location of the video?\nAssistant: The video takes place in a cozy room with wooden walls and a large window adorned with pink curtains.\n\nUser: What is the setting of the video?\nAssistant: The video is set in a cozy room with wooden walls and a large window adorned with pink curtains.\n\nUser: Where does the action in the video take place?\nAssistant: The action takes place in a cozy room with wooden walls and a large window adorned with pink curtains.\n\nUser: What is the background of the video?\nAssistant: The background features a wooden wall and a window with pink curtains, allowing natural light to fill the room.\n\nUser: What landmarks or objects can be seen in the video?\nAssistant: The video shows a wooden wall, a window with pink curtains, and various props like crowns and a black case.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['jungle', 'speech event', 'stage', 'classroom', 'park'])=<b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

