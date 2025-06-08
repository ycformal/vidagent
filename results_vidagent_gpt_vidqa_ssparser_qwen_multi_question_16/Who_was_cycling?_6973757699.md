Question: Who was cycling?

Reference Answer: 0

Video ID: 6973757699

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="Who was cycling?|Who was riding the bike?|Who was on the bicycle?|Who was pedaling?|Who was moving on the bike?|Who was balancing on the bike?|Who was steering the bike?|Who was wearing a helmet?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="Who was cycling?|Who was riding the bike?|Who was on the bicycle?|Who was pedaling?|Who was moving on the bike?|Who was balancing on the bike?|Who was steering the bike?|Who was wearing a helmet?")
SELECTED=SELECT(question="Who was cycling?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA4AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwC4+o+NdamMNor2ik9EjVMf8CY5/SpZdC8UWpjuLu4ti2f9dLKZWQ+wI/lWpD47tY12WdldXchPG1MbvyBqG81vXtVt2jGgvCOuWjzt/wC+mH8qheSOiyQ9bDUrtEW4165kL9fJiIz9M1s23hDTHjYTNd3RXl/Mkb+QbFZmnP4nmhWIeUi9Av21Iv0RSf1q6lhrNuNkwsIwT1lmlnAz7cCrSe4aFS80rQrCQ+QthFju0KEg++QTXnHjLw+Z76znt7mK5kuTt+X73+8VAGAPevUktbyytZmTV7GILl3aGxG7p7sa4nV79Z9QeS6crFGi4jGACx5YkDvk/pUzegpJNGVH4Fg8P31x5WoNe36yBI3RAkaIep5JJc9AB0zmtO+8F6TpFrGZrK7hec+c0s868YPO1Vz69yKxD4mhsWH2aKUODkHoAPbvn3qnL4ll1DEe35cBCZXL7R9ay1EoxtY2r7wjpWp6c9/arDollbkK0iEtv4H94/Mx6/jXnN/o9lHLkSTMvO1ncZI98DivR73Vk1HSbTRrTTbSMRof9ImcuSwBJOM8ZPt6CvONP1Oe38Q2r3EoZYrhSylQVOD0I9K7aM6cYO6uxODsatl8LdavHgAAVZ03xnaclcA5+nI5960E+F09pdrbXn2mSZkMixxR4O0HBPU11V58QZ4dTjuzGEZVdAqYYLux2/AVTsPHzvr8d5emSSARmJgvJUHGcD6gVhJ9hqBDF4Ujt4xEdBZyvG54CSfqcc0V1Fx8T/scgi0ywF1b4z5kkvlEnuNporLmZooo3l8VQTSm3Oj6nvXqkcQOPyq8mq6f9ldpdO1C3BHWS1Y5/LNYemP4wtrMsWsdqnJLqQT+NLN4i8WlvKWytZMHBMbnmtVC5NzRhudKkb/Rri3WU/35dhH4Grrana2C5l23DntG/mZ/CuQvvEGtwsI77wwkmTg5G4H9KY09ldoPNsrSxlx1jLRkVXIIveKPFtqbFoYmW0lx5rxswDMo6AD3NcXpcA1K2ned/Ol8wlFVskZzkk5/p2q1qkF9Kxt5Ft3SY+UJZBuYqPmJz6YFYkptdLJljjj4GQYnMZP64NJpdBPzNW/sdPsbGeK7T/TJAPKkQjaBjkf/AF6bpPhYXNgZ4rKeKC4PyXU7KkXB7O2PfpmucDxa7cw20b3aBssHJUlh6Ek9ue3JPtVXVrvWp70WG5ksIWKRQyHckYHH54AqlTNIwXJzv+v8j0CXw7oOioZ9R8TxzXAU7LbTkD447sa8x1izhiZJIQcs+M+p61uDTL+5tvtFlZNKg42QqcfUD0rSksIZ7WCWS3aN0UExOuCp75Fawho0hxUZXjcrRWtpfaSsy25jlEXmYDAk446fUVnIzRRMscREjHBwv3QetWL+B1mNxG205GEHXPqP0qD+1fsTs00KszjH+TWM48srMTsh8RlMY2LHjvuJBzRWc+p5kYrGoUnIFFYuF2Toz6Bgu7WWNFnuSzHOUHSui0/7HDbrsZVJ53Fc1zeg6NFFAJpnYEk8MCDXSxLbQKCy+2TkitUrIRZkubMneSWx/sk1z+o2tpeSvmNWX72GjzjjtWncvaD53MeG6fNiqctpp13YXEM7okU8ZVn3YKgjqKWwHmGvESeKNH0W2vRGskE8ssqgNnj5Rt9fl6e9ZVxo1vpkgcRR3SqeZC37z64PANZdxYala61biOG4W4sJioZ4Dgqcg89Dwc1enu7gErc3Ch8Z2bdzEfRRmhc03aKEk27EMF/pY1WKZLNBcQkus8shVSMdSBxnpj8qq3unfabeOZr2V7ovvm+UfP8ASq91eWkzIJJ/KMzFMhSvTHBBHTJ/Snp9t0vLIC8IO51ZT0/z6Vs+eFovc740LJU3JX7dNfNHX2fjNrqWPTrgCEhDhyp8tVUdMKM9BXN3HiKC5uLhQHYI20SIuQ69jg81k312L8xTSbIIwhDNHn58k9vXBxmpHjto9CkuIL+0XauETzAXJPYj1r2JV0qS9p16I8hQVKtL2S1LUk9xLAlzZ/cQ8+Yg5PY4NZ1xceewN6F55LR4xn6VhjVLsRGPzvlJyfep3v8A7aAryJAMEEgcdPSvGqXlJytodDbe5f3WRAIuQox0Jorm9vuaKysTdn3MYVPXP50oiXpj9aKKsxuxPs8JbcYkJ9SKivJY7GxnuNq/u4ywGOpxwPzooqQTbOM+IVxc+HvhwIrZsTyPFbPKeSC5+Y/ic/nXlIuZbBHt7FnjhiBZtvDPjqzEcsfr0ooraid+EoxqRnKXS34tI4XV5ZtTu5rpiWCnIJr6e8PaXHZ/DiyjlYXDnTwQbrb0dMhCe4GdvPYUUUVHrcwq1JObfmfO+raO2mw7TtaGZyYgP4V78/lXLQW6CaUybcxtgKTweuaKK7ay9xLzNqiTxM3bc7XwHqOrLrEtvpuj2movLCVEDr0Uck+np19qnmvodG1M6rDotii3LSW1xp5bzIQyhSHU84PzdB7+tFFcrim7GNVcr0OQuYHu7mW4cKrSsWIRQqjPoB0FFFFW6cTK5//Z">, <b><span style='color: darkorange;'>question</span></b>='Who was cycling?|Who was riding the bike?|Who was on the bicycle?|Who was pedaling?|Who was moving on the bike?|Who was balancing on the bike?|Who was steering the bike?|Who was wearing a helmet?')=<b><span style='color: green;'>User: Who was cycling?
Assistant: A young girl was cycling.

User: Who was riding the bike?
Assistant: A young girl was riding the bike.

User: Who was on the bicycle?
Assistant: A child was on the bicycle.

User: Who was pedaling?
Assistant: The child was pedaling.

User: Who was moving on the bike?
Assistant: A child was moving on the bike.

User: Who was balancing on the bike?
Assistant: A young girl was balancing on the bike.

User: Who was steering the bike?
Assistant: The child was steering the bike.

User: Who was wearing a helmet?
Assistant: The child was wearing a helmet.

Note: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=Who was cycling?, <b><span style='color: darkorange;'>information</span></b>=['User: Who was cycling?\nAssistant: A young girl was cycling.\n\nUser: Who was riding the bike?\nAssistant: A young girl was riding the bike.\n\nUser: Who was on the bicycle?\nAssistant: A child was on the bicycle.\n\nUser: Who was pedaling?\nAssistant: The child was pedaling.\n\nUser: Who was moving on the bike?\nAssistant: A child was moving on the bike.\n\nUser: Who was balancing on the bike?\nAssistant: A young girl was balancing on the bike.\n\nUser: Who was steering the bike?\nAssistant: The child was steering the bike.\n\nUser: Who was wearing a helmet?\nAssistant: The child was wearing a helmet.\n\nNote: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.'], <b><span style='color: darkorange;'>choices</span></b>=['little girl', 'boy in shorts', 'monkey', 'lady', 'man in red'])=<b><span style='color: green;'>0</span></b></div><hr>

Answer: 0

