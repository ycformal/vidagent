Question: How did the lady ensured she can see the boys clearly?

Reference Answer: 3

Video ID: 2965378944

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How did the lady ensure she can see the boys clearly?|What is the lady doing?|What surrounds the lady?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How did the lady ensure she can see the boys clearly?|What is the lady doing?|What surrounds the lady?")
SELECTED=SELECT(question="How did the lady ensured she can see the boys clearly?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDxkuYAxB6Dmut0jXredLezu5IkS3hDRu5wDkDI+oIP51ylxbyT3Jt4kYuxIxg8cVctPCdzdXPlmdEJPIxk1E3G1mxxvc9Pt7iO48MXL2l1EEWTDXGQRCMDcw/2guSPfFdP4dCjSLRUtzbIIgEhbqi9gffGCfrXI6RpUOneGbq1toVuG8xH2E4DPkYLei5AJ9ga6/w8yPpNuyTvcKUz5zjBk5OW/E5I9sV5svjf9f1/XmdC2NXBBpG5B+lO6VE74UnBJ9BTGVHHNVpOTU8kyLksGVQCSxGABUCyJNGskbq6OMqynII9QaYyE00jipSOar3Unk28j+ik1IHOW7Lc+MoJGGYoi0hP0GBXbR3NtIu3z48e5x/OuG0CMy3t7c8nGEH071vOHV8bTgcZroi7I55q7NG5kjjlwNrAjOQQaKoIBtyVXJ/2aKvmJscJaw3E8pby4oYTwNq8H1/ya2bOzhjRUkLSv1JIABP0rItrua/usaZZmdBwLi4OxAfp3rWj0MsgfWdSkaHr5akQpn39ah+ZqkXGv7F9F1WJXEnkxAyxQHkjP3TjoD0J9Ca6nw3ObnQ7O4MkbmSIMTEMLz2A9B0/CuetbfTI9Ku49MA2mPLfZCC5H90H1PT8a6TQ8/2VAGECsFwUgOUXBI2r7Dp+FYytzGq2NIt6GsXWPEFhpHyzyqZj0iB+b/61XdTvF07Tbm8ZWYQxl9qjJPtXi19brezzX8rkTEfvIkcltxP+eKuEU9wPXbC+i1SyW5i2mOQZA609sJwFAA6ADArzPwFdy2fiQ6fDdNNayQsXUnhWHII9+1elyVM48rsCGE5rJ1u4Edk4yBnqfbrWoWArm/EE6YCM3ylgDxnPPPH0qFuBnaaLhIF8m5kiZwXPyjbn3yKuPdakCVSXdHn5d6jkdOoqfRJDf6THKyrH1254LKGOD+IFWfsx8wYPbjB4x9RWl2tDBopLq15GNphibHGckUVaZIlO0xtkehxRRzE2Zm6hrFtp1s0jPhI/4V52/lXI3k82rTCSTUI5cnKrtYAfQYqnp+m3N/E0FtA8oKM8m1c4xwK6zQNNMPiLULeKAokMUQRSOfmGSefpXQoqPqbNotaTLp+jaJPE89xCZIy7zKhDdOq10nh7XrCPSIVmAtgiYCJE+xBnhc47Dgk981514lVrrU47KCF5JLeR3lXdgBOMr1647e9djJr1pbW8llKXRr1W8tYyGCZGOTnGcYOKznTvqVCSejO+t4Y9QtI58B7WYZXcpxIAfT0OK5i98F6JaTXsmlmJJcGWcXJI8sE5AB5Hv74rtdb1+30rw+JZgqR2sIWMKMsxwAB/LisHQvAkWvGTUfFN8xe5QbdOgmMaRjr8/Tc3PTtzVQp3bUdhOp7NXn12PGoYD4ejfVoblJ0uJWSExN1I5O444+g5rufC3id9fiME0eL5TnYqEbl9RXT/ABD8K6WPCEul6OkYOmIbgIgHyMoyFz/eYEn1rx3Qdeksddt71ZP3W8H5/m2DsQDwD7/WqqUtNRUqinqz1DUbhNPgklut0YXqMc5rhb7Wf7QuvLEMsYBJU4znsDXTeKdWt/ElhHJDND9rAMUskf3ZMYIz2z1plvb21zoNu1nJCsqDDgY3Ee1c0UuprbQv2BtprOE2wBt1TYu7gjbx/SrPlo2csQevArF8JM3kzW+1lEbHJzznPpXQOWBypOPbuKbMWiubNmOduc+pxRViSRQ3+rV/cnmikKxyNyZdI1TTRY26F2XyFgDFQ7ZBUAjnOehHevXtX0mzg0cR68hdbtRAFHzOjkZH7wYIxgjPrXiOj3z6r8WNGjgLPHay7tznhDg4YnsAcV77qzy63ZjT4rdbvhS8pX5Nw7g9uea6rNRv1HN62PH5vhNex6/bwaTq9oLRn3xSSRt5wfbyj44Jxz2zzXO+O/h74n8MStqEscM1gzjddWqnZG3QFlPKn36e9fQFvoM0Gt2k8jDy41E0/PyowVlGPUncfwFZHxV8W2Hhvwy73beZd3sckEFicYlRlw2/uAMg5HfAq4tt3aIbsc74MufDXiSy06XUr+WS9skCvbyTqUMi9JNvU9iOo/EV12q3mjWUJX7YY5GQsrs4wPfoc18gRyzRSLLEzI6nKspwQa9D03xzrYsFW5isnmjGEkmgy/Tr1xn3xWyinokc8027tnoKX1wPCfiqa4ikET3E2xpMlmzGAQe+RgA/l2ryPw1pkFzaLczSyIVkxs2ghwPr/nitrS9d1K+8N6vC7yTzzT4Y4zhWySB6csx/GrE2kDRrbTYo7hZo5rcNvUdHH3lI9Rn9a5neLZ2JJJWNvRbKGNZ51kgXeu1vMjwjcYOQO/IxWNJot/bXEqJE/wBmOfKy23kda6uG3jjWGJUeRFG0Bevrkdef8a4rUfF8h8QrOsU8dnEPJaFn3ZAzk9Bg1xRlKpJtHtvDU6dNc+5oW93b6Da2d5azkwiTbeIzjdh+M49VOK70HhQG3DHDDvXz7czi6vXfHyZyRn1r1XwFrX9o6QtnO5NxZkJyfvJ/Cf6fhXVOnZXPD5rs6ebYJP3itn6kcUVKSrMTt7/3c0ViB5j4M2aPqmoXLyx3TXNs9vFHEdx3sRjI9vbvivW/D3xKGj6dbafd6VMYoYgisjHdgdyGryf4dRI3i3SwVHEpIxxzg19FW8aSSqjqGUvggjOen6+9dzCTj2Ma7+LGiCxmnjt7uWaJSYrbyxmR8cZIOBzXzZ4qvvEXinXZ9V1WCdppDhVCnbGvZVHYCug8c31zeeOdTSeUlLePESqAoXj2xn8ayklkSwkdZH3KJCDuPGMYqlFpXDlg1fUwraI2g3yWVwXHcrjH0rUivhPCYmtpYhjKuYmb+Xaokv7sNEPtD8gE8+1aNhfXMhIeViN4HPpQ6rQ1QjLW4+38Uf2NaRx2OZAq7ZP3ZXJ9cEYpttr6arqUY8txLjYiHkuSegAFabOw3AHjeRjHatfwVt/4S3Tn8uPdvb5vLGeh9qxcl2NFRfRnR6PpWo3cMStapA6Y3GVzu+uB6/WvMPG66dBrd2unyo21sMEXA3/xY5PGa9a+I15cRS2AjmdNySFthwTjGOlfPMsjNO7FiSSSSe/NZ0KMbuSN6+JquCUmOtyNnvmtrw/q76LrVvecmHOyYDuh6/l1rABI6cU8O2MZNdfJc89Hv0F9BdQrNazJJC/KupOGorxiw8RaxZWwgt9QmSJDhVzkKPQZ6CiuV0bOxXOj/9k=">, <b><span style='color: darkorange;'>question</span></b>='How did the lady ensure she can see the boys clearly?|What is the lady doing?|What surrounds the lady?')=<b><span style='color: green;'>User: How did the lady ensured she can see the boys clearly?
Assistant: spectacles

User: What is the lady doing?
Assistant: The lady is pushing the wagon.

User: What surrounds the lady?
Assistant: The lady is surrounded by a grassy field, a few buildings, and other people in the distance.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How did the lady ensured she can see the boys clearly?, <b><span style='color: darkorange;'>information</span></b>=['User: How did the lady ensured she can see the boys clearly?\nAssistant: spectacles\n\nUser: What is the lady doing?\nAssistant: The lady is pushing the wagon.\n\nUser: What surrounds the lady?\nAssistant: The lady is surrounded by a grassy field, a few buildings, and other people in the distance.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['hold hands', 'by hand movements', 'make eye contact everywhere', 'spectacles', 'follow the children'])=<b><span style='color: green;'>3</span></b></div><hr>

Answer: 3

