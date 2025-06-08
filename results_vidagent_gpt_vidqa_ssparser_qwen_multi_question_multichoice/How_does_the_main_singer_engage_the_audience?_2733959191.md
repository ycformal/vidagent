Question: How does the main singer engage the audience?

Reference Answer: 2

Video ID: 2733959191

Original program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VQA(video=VIDEO,question="How does the main singer engage the audience?|What is the main singer doing?|What surrounds the main singer?|How is the audience reacting?")
```
Program:

```
TIME=FLAG(begin=None,middle=None,end=None)
ANSWERS0=VIDQA(video=VIDEO,question="How does the main singer engage the audience?|What is the main singer doing?|What surrounds the main singer?|How is the audience reacting?")
SELECTED=SELECT(question="How does the main singer engage the audience?",information=ANSWERS0,choices=CHOICES)
```
Rationale:

<hr><div>FLAG is only for internal use.</div><hr><div><b><span style='color: blue;'>ANSWERS0</span></b>=<b><span style='color: red;'>VIDQA</span></b>(<b><span style='color: darkorange;'>video</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDtP7SgUiMbd390EcfWhdYtWZgswIUfMQeBXmhX5sFhz1+Y0AZOdx2+vIoA9JTWrVwzeaoUdyw//WaU6zbKu4yYBOB2z/n2rzQKA2SwHqSeacQehYnHTJP8qAPSTq1uqgs6gsflXcMmg6vbjC+YGJ7KRx9a81AC8hwOc4yTz+dGCcY3Zb1JoA9KOr2xfyxIpcdRu4pF1m1dyBIML949AK81ChT8hC5OOp6UuAckk7V4GTigD0ldYt2yWdQOuS3X6DrSHW7URl/NXHQfNjNeb9OC+PqT/KgLx1bP4/5NAHpLa1aqFBlXLDhdwJ/LrQ2r24cRF1L/AN0Hp9fSvNQFG4k49cck0bOMnBycckgUAekvrdojbTICR1wRj+dFeaudrbQ4AHq5FFAEazYOQR142j+tL5j/ADNjr3Y4q6NPj2BSN395s4JpGsYCB+7wRx0JOPrQBRE20YDDr/CORQ0rYzjHPVj/AIVfNjCduFl47biKZ9hg3H93L65APNAFRZiW4xj/AGOc0pkycnhR/ebFWls4wc7ZTnpuGactnEqYCNz94lSSaAKXnYJOc8/wj+tJ5jB+cdMfMattaRY2+TN16gHp6UNaQnpbSrg/LtQ8/maAKgmbbtU8dflXH5UrSFgMAA+pOc/Srhs4SeIZQOvcfypRZwAk+XIQeOVyfz60AUvOJPBznsoxn86RpT3AAHXc3Srf2OLk+Xc5IxwCcULaxFAgglU55by8H8DmgCm0wJyZAPoOKKvmxUnIjfHYZFFAB/wl+jCMsRe49fsb4P6Uv/CXaMCp23Y3dALOQ/lxWEviOzE7IulakA3TNqck9OQDk/nR/wAJBaqoWTSdRQr94m3IPXpjdmgDbbxhoqLl/tig8gmzcZ/SkPjHRQvAuySMjFo5z+grHfxDbxDjSL7JGWDQbep6ABs5xSTeILRZFD6Teqecr5OWIzwcBsjigDaHjHR2+ZYdQYYyQtm1IPGGkMGxDf49rJzWP/wkFsZNq6RfjkH/AI9/nAPsDk0Nr9sJh/xKNSTeflzb5OB6jPP6UIDYk8Y6OgAMOobm4H+hsM+1OPi7S1Cs1tqChuADZPzWN/b9u2yM6RqC9RzbYbPbjdznjvSP4gtxFsfS7tJE4ZRDuI+ih/egDX/4TLRySvk6ic8gCzan/wDCXaWyZW31DHTIsnrIl1+2dAI9GvlPP/LDJYY4JAIpr6/asfKGlahzyo+y7j+OG470Aa7eMdIUAm31HAOCDZsBQfGOkrkPBfqOn/Hm1Zb69bs3lx6PqHXKZtstj6AgetRN4jhCFf7HumLZHyopJ56kbjj3FAI3B4x0lflaDUQRwQLNqKwk8SQxrsOiXsZXssaDPv1oo0Fc5tPFdtC0zxickt+7DRjj6/Nj1oHii0EUoV7lGJIj/dggL/311684OKgfT2GN9hpqDGTJtmx1+pBpj2DB8C30k4H3WZ0+nUjn2zSTuWo3Rdm8T6W+NqXi4XbnaCXHfccjv6Uj+LbF0iEcFxbuu5naMKdzHGBjI49apx6XcMVL2WnAFThVYufxw+aeNNdUZjb2A24zuglxVNWM27E6+LrcM+YpWDENuKDIPsN2MfXPQUDxZbR3TyxJcCNjkRlRhD3I+bBPfkVWbT59xKWmlNhecbxg+hBPWkOmziJXlsrFQRgBUdvx+VjUp3LSuWE8UWIiZHguX/utkAnuM844+lI3im0a2Eaw3MUgyN6kEkdgenf/APVVb+ziqN8umBtpPzJJgD1z60/+y7obSLLS3D8Aq5P6bv6VTjYmTsWX8W2kiqn2aZccs64yTjHrj1/M8VDH4rSNkBEzRjO5FRUzxjqDR/Zcnyg2dinHJMMhxjr3NRvYSfLtt9LKkc5DqVHqcmovrYqKuTp4ptPNDSRTuhHzJtXr3xk9+OoqQ+K7A7x9nuArcYyDx25yOh5FVhpkiKGa2sDxjbsZv5NmmjTTxmLTYyf76SjA9/T/AOvV2FJ2LUPi+CCMIkErAd35JPvhgP0oqs9g6kBk0JDjoXYH9TRU8xHOA8Q2DqFls+ApBeNBG5546HH+e9Rxa5bw7GSW6LDqJERhj0x0/GucoplnSjWrB0HmRPuGTzEjYPtmo31qz3q0QuYCBn9yQBn2BJwOn5dK57pRQB0MniLzkCzSXEmGzllTp6Ed6VdftArK9osgxkExhWU47EH1rnaKAOlXxBZoEEaXkQzuZQ6sCfQZ6Cojrtuz7nid+SRujQkfX+99eK5+igDoBrdkC2LV1xlk2fLg5PoenPvTofESwKgWW8YZy4fY2fpmudooBnRJr1oPLdoWMgPO6JGGPrnJo/t6yyHW1mhk3Z/cyYUDtgHP+RXO0UAdD/wkj9BLOQO7qpP9KK56incd12P/2Q==">, <b><span style='color: darkorange;'>question</span></b>='How does the main singer engage the audience?|What is the main singer doing?|What surrounds the main singer?|How is the audience reacting?')=<b><span style='color: green;'>User: How does the main singer engage the audience?
Assistant: touch their hands

User: What is the main singer doing?
Assistant: The main singer is singing passionately.

User: What surrounds the main singer?
Assistant: A group of backup singers and dancers surround the main singer.

User: How is the audience reacting?
Assistant: The audience is seated and watching the performance attentively.

</span></b></div><hr><div><b><span style='color: blue;'>SELECTED</span></b>=<b><span style='color: red;'>SELECT</span></b>(<b><span style='color: darkorange;'>question</span></b>=How does the main singer engage the audience?, <b><span style='color: darkorange;'>information</span></b>=['User: How does the main singer engage the audience?\nAssistant: touch their hands\n\nUser: What is the main singer doing?\nAssistant: The main singer is singing passionately.\n\nUser: What surrounds the main singer?\nAssistant: A group of backup singers and dancers surround the main singer.\n\nUser: How is the audience reacting?\nAssistant: The audience is seated and watching the performance attentively.\n\n'], <b><span style='color: darkorange;'>choices</span></b>=['walk forward', 'jump down stage', 'moving while singing', 'touch their hands', 'motioned with his head'])=<b><span style='color: green;'>3</span></b></div><hr>

Answer: 3

