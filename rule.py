import ast
from collections import Counter

# The data you provided as a single multi-line string
raw = """
{'ending off': 10, 'see where the ball is falling': 5, 'to throw it': 5, 'finished watching the peacock': 10, 'showing his joy': 70}
{'ending off': 50, 'see where the ball is falling': 5, 'to throw it': 5, 'finished watching the peacock': 1, 'showing his joy': 39}
{'ending off': 10, 'see where the ball is falling': 0, 'to throw it': 0, 'finished watching the peacock': 0, 'showing his joy': 90}
0
{'adjust head': 10, 'walk to the store': 5, 'takes out notes': 50, 'cry': 5, 'drink water': 30}
{'adjust head': 60, 'walk to the store': 5, 'takes out notes': 10, 'cry': 5, 'drink water': 20}
{'adjust head': 80, 'walk to the store': 1, 'takes out notes': 5, 'cry': 1, 'drink water': 3}
2
{'playing the guitar': 5, 'wave at girl': 50, 'take more food': 20, 'look down': 15, 'eat': 10}
{'playing the guitar': 5, 'wave at girl': 20, 'take more food': 10, 'look down': 60, 'eat': 5}
{'playing the guitar': 5, 'wave at girl': 85, 'take more food': 3, 'look down': 5, 'eat': 2}
1
{'five': 5, 'two': 85, 'four': 5, 'seven': 3, 'one': 2}
{'five': 5, 'two': 40, 'four': 15, 'seven': 1, 'one': 39}
{'five': 0, 'two': 5, 'four': 0, 'seven': 0, 'one': 95}
4
{'street': 15, 'avenue': 10, 'playground': 5, 'snow mountain': 5, 'garden': 5}
{'street': 5, 'avenue': 5, 'playground': 15, 'snow mountain': 0, 'garden': 10}
{'street': 5, 'avenue': 5, 'playground': 5, 'snow mountain': 0, 'garden': 40}
4
{'near a staircase': 10, 'golf course': 15, 'home': 30, 'stage': 25, 'theatre': 20}
{'near a staircase': 5, 'golf course': 5, 'home': 80, 'stage': 5, 'theatre': 5}
{'near a staircase': 85, 'golf course': 5, 'home': 5, 'stage': 3, 'theatre': 2}
0
{'play an': 10, 'boat': 40, 'wooded areas': 5, 'hospital': 5, 'outdoors': 80}
{'play an': 5, 'boat': 5, 'wooded areas': 5, 'hospital': 5, 'outdoors': 5}
{'play an': 5, 'boat': 50, 'wooded areas': 20, 'hospital': 5, 'outdoors': 20}
1
{'toothbrush': 5, 'moving toy': 5, 'blue bowl': 10, 'elmo toy': 5, 'pacifier': 5}
{'toothbrush': 5, 'moving toy': 20, 'blue bowl': 70, 'elmo toy': 2, 'pacifier': 3}
{'toothbrush': 5, 'moving toy': 80, 'blue bowl': 10, 'elmo toy': 3, 'pacifier': 2}
2
{'two': 85, 'three': 5, 'four': 3, 'five': 3, 'six': 4}
{'two': 10, 'three': 25, 'four': 50, 'five': 12, 'six': 3}
{'two': 95, 'three': 2, 'four': 1, 'five': 1, 'six': 1}
0
{'guide dog while running': 80, 'get food': 5, 'walk away': 5, 'throw ball': 5, 'follow another adult': 5}
{'guide dog while running': 10, 'get food': 5, 'walk away': 5, 'throw ball': 75, 'follow another adult': 5}
{'guide dog while running': 95, 'get food': 1, 'walk away': 1, 'throw ball': 1, 'follow another adult': 2}
0
{'pose for camera': 5, 'catch baby s attention': 5, 'reach for the ball': 80, 'striking a pose': 5, 'diving position': 20}
{'pose for camera': 10, 'catch baby s attention': 5, 'reach for the ball': 5, 'striking a pose': 10, 'diving position': 70}
{'pose for camera': 5, 'catch baby s attention': 0, 'reach for the ball': 0, 'striking a pose': 10, 'diving position': 85}
4
{'move away': 10, 'throw the toy again': 20, 'ignores': 30, 'wait': 40, 'stay still': 40}
{'move away': 25, 'throw the toy again': 5, 'ignores': 15, 'wait': 35, 'stay still': 20}
{'move away': 5, 'throw the toy again': 0, 'ignores': 5, 'wait': 10, 'stay still': 80}
3
{'three': 5, 'six': 1, 'two': 85, 'one': 9, 'five': 0}
{'three': 5, 'six': 1, 'two': 10, 'one': 80, 'five': 4}
{'three': 0, 'six': 0, 'two': 5, 'one': 95, 'five': 0}
3
{'retract her hand': 70, 'crawl away': 5, 'turned behind': 10, 'touch girl in black': 10, 'get out of car': 5}
{'retract her hand': 40, 'crawl away': 10, 'turned behind': 10, 'touch girl in black': 15, 'get out of car': 5}
{'retract her hand': 5, 'crawl away': 1, 'turned behind': 1, 'touch girl in black': 10, 'get out of car': 1}
0
{'mother child': 70, 'grandmother grandson': 25, 'father and child': 1, 'teacher student': 1, 'sibling': 3}
{'mother child': 75, 'grandmother grandson': 15, 'father and child': 0, 'teacher student': 5, 'sibling': 5}
{'mother child': 40, 'grandmother grandson': 50, 'father and child': 5, 'teacher student': 3, 'sibling': 2}
1
{'plush toy': 80, 'water bottle': 5, 'tape': 5, 'red train': 5, 'bat': 5}
{'plush toy': 10, 'water bottle': 5, 'tape': 5, 'red train': 20, 'bat': 25}
{'plush toy': 5, 'water bottle': 5, 'tape': 5, 'red train': 80, 'bat': 5}
0
{'move backwards': 5, 'run towards lady': 10, 'it stopped moving': 5, 'bite the toy': 40, 'fetch the toy': 80}
{'move backwards': 10, 'run towards lady': 30, 'it stopped moving': 5, 'bite the toy': 40, 'fetch the toy': 70}
{'move backwards': 5, 'run towards lady': 1, 'it stopped moving': 10, 'bite the toy': 15, 'fetch the toy': 5}
3
{'one': 5, 'two': 20, 'three': 70, 'nine': 1, 'four': 4}
{'one': 5, 'two': 30, 'three': 60, 'nine': 0, 'four': 5}
{'one': 0, 'two': 0, 'three': 0, 'nine': 0, 'four': 100}
4
{'open its mouth': 5, 'stretches': 10, 'faces the cat': 30, 'caress cat': 35, 'open the bag wider': 20}
{'open its mouth': 10, 'stretches': 15, 'faces the cat': 25, 'caress cat': 20, 'open the bag wider': 10}
{'open its mouth': 5, 'stretches': 5, 'faces the cat': 10, 'caress cat': 10, 'open the bag wider': 70}
2
{'touch the cake': 10, 'blow': 80, 'put into his mouth': 5, 'run away': 2, 'grab the candles': 3}
{'touch the cake': 10, 'blow': 70, 'put into his mouth': 5, 'run away': 5, 'grab the candles': 10}
{'touch the cake': 70, 'blow': 10, 'put into his mouth': 5, 'run away': 5, 'grab the candles': 10}
1
{'run to woman': 10, 'drop bottle': 25, 'move to table': 5, 'step backwards': 50, 'hit goat': 10}
{'run to woman': 10, 'drop bottle': 15, 'move to table': 5, 'step backwards': 60, 'hit goat': 10}
{'run to woman': 5, 'drop bottle': 5, 'move to table': 5, 'step backwards': 10, 'hit goat': 25}
3
{'nine': 0, 'six': 0, 'one': 20, 'two': 75, 'three': 5}
{'nine': 5, 'six': 5, 'one': 20, 'two': 65, 'three': 5}
{'nine': 0, 'six': 0, 'one': 95, 'two': 5, 'three': 0}
2
{'looks at the toy': 20, 'open her mouth': 10, 'smiles': 60, 'put her legs on the table': 5, 'cry': 5}
{'looks at the toy': 5, 'open her mouth': 25, 'smiles': 20, 'put her legs on the table': 0, 'cry': 0}
{'looks at the toy': 10, 'open her mouth': 70, 'smiles': 10, 'put her legs on the table': 5, 'cry': 5}
1
{'push swing': 5, 'pick up the present': 5, 'look back': 15, 'rode backwards': 20, 'hit the ball': 5}
{'push swing': 5, 'pick up the present': 5, 'look back': 15, 'rode backwards': 10, 'hit the ball': 5}
{'push swing': 5, 'pick up the present': 5, 'look back': 85, 'rode backwards': 5, 'hit the ball': 5}
3
{'pick up cups': 5, 'lose balance': 70, 'shoe fell off': 5, 'to pat it': 5, 'still learning to walk': 80}
{'pick up cups': 5, 'lose balance': 40, 'shoe fell off': 5, 'to pat it': 5, 'still learning to walk': 45}
{'pick up cups': 5, 'lose balance': 70, 'shoe fell off': 5, 'to pat it': 5, 'still learning to walk': 60}
4
{'plays the instrument': 5, 'stand still': 20, 'start crying': 1, 'move head around': 25, 'claps': 49}
{'plays the instrument': 5, 'stand still': 30, 'start crying': 5, 'move head around': 50, 'claps': 10}
{'plays the instrument': 5, 'stand still': 10, 'start crying': 5, 'move head around': 80, 'claps': 0}
3
{'four': 1, 'nine': 1, 'two': 95, 'six': 1, 'five': 1}
{'four': 25, 'nine': 5, 'two': 10, 'six': 30, 'five': 30}
{'four': 5, 'nine': 5, 'two': 5, 'six': 5, 'five': 10}
2
{'listen to him': 40, 'stop running': 10, 'pointing and talking': 45, 'walk along the lighted up wall': 5, 'nod to him': 25}
{'listen to him': 30, 'stop running': 5, 'pointing and talking': 10, 'walk along the lighted up wall': 5, 'nod to him': 50}
{'listen to him': 10, 'stop running': 80, 'pointing and talking': 5, 'walk along the lighted up wall': 2, 'nod to him': 3}
1
{'sit down': 20, 'look at mirror': 5, 'look down': 30, 'look up to the person next to him': 10, 'play with rabbit': 35}
{'sit down': 10, 'look at mirror': 0, 'look down': 60, 'look up to the person next to him': 20, 'play with rabbit': 80}
{'sit down': 5, 'look at mirror': 0, 'look down': 10, 'look up to the person next to him': 80, 'play with rabbit': 30}
3
{'walk away': 10, 'run forward': 70, 'run to his right': 15, 'listen to the music': 3, 'play with baby': 2}
{'walk away': 20, 'run forward': 50, 'run to his right': 25, 'listen to the music': 2, 'play with baby': 3}
{'walk away': 20, 'run forward': 15, 'run to his right': 50, 'listen to the music': 0, 'play with baby': 0}
2
{'head band': 10, 'hair clip': 5, 'necklace': 0, 'tiara': 0, 'cap': 85}
{'head band': 90, 'hair clip': 5, 'necklace': 1, 'tiara': 1, 'cap': 3}
{'head band': 95, 'hair clip': 2, 'necklace': 0, 'tiara': 1, 'cap': 2}
0
{'dancing': 0, 'drawing': 20, 'painting': 80, 'drinking milk': 0, 'sleeping': 0}
{'dancing': 0, 'drawing': 85, 'painting': 80, 'drinking milk': 0, 'sleeping': 0}
{'dancing': 0, 'drawing': 10, 'painting': 90, 'drinking milk': 0, 'sleeping': 0}
2
{'eleven': 5, 'three': 20, 'four': 10, 'one': 5, 'five': 60}
{'eleven': 5, 'three': 10, 'four': 40, 'one': 5, 'five': 40}
{'eleven': 0, 'three': 0, 'four': 0, 'one': 0, 'five': 100}
4
{'laugh and shake body': 5, 'wag its tail then stand up': 40, 'play with instrument': 0, 'open mouth and bark': 50, 'move away': 5}
{'laugh and shake body': 5, 'wag its tail then stand up': 70, 'play with instrument': 1, 'open mouth and bark': 15, 'move away': 9}
{'laugh and shake body': 10, 'wag its tail then stand up': 80, 'play with instrument': 0, 'open mouth and bark': 5, 'move away': 5}
3
{'looking around': 10, 'play with it': 5, 'swipe person hand away': 5, 'resting': 75, 'lie tightly besides the person': 5}
{'looking around': 5, 'play with it': 5, 'swipe person hand away': 5, 'resting': 80, 'lie tightly besides the person': 5}
{'looking around': 80, 'play with it': 5, 'swipe person hand away': 5, 'resting': 40, 'lie tightly besides the person': 10}
0
{'quickly': 5, 'did not move': 85, 'speedily': 5, 'hurriedly': 5, 'slowly': 10}
{'quickly': 5, 'did not move': 50, 'speedily': 5, 'hurriedly': 5, 'slowly': 35}
{'quickly': 5, 'did not move': 0, 'speedily': 5, 'hurriedly': 5, 'slowly': 85}
4
{'sit down': 10, 'stop at the door for a while': 70, 'put toy on counter': 5, 'raise both hands': 5, 'put hand in mouth': 10}
{'sit down': 10, 'stop at the door for a while': 50, 'put toy on counter': 25, 'raise both hands': 5, 'put hand in mouth': 10}
{'sit down': 5, 'stop at the door for a while': 10, 'put toy on counter': 60, 'raise both hands': 5, 'put hand in mouth': 5}
1
{'two': 80, 'one': 15, 'kitchen': 0, 'three': 3, 'four': 2}
{'two': 5, 'one': 90, 'kitchen': 0, 'three': 3, 'four': 2}
{'two': 5, 'one': 90, 'kitchen': 0, 'three': 3, 'four': 2}
1
{'anxious to eat cake': 10, 'upset': 5, 'talk to man': 20, 'reluctant to leave stage': 5, 'taking photos': 60}
{'anxious to eat cake': 10, 'upset': 5, 'talk to man': 70, 'reluctant to leave stage': 10, 'taking photos': 5}
{'anxious to eat cake': 5, 'upset': 5, 'talk to man': 10, 'reluctant to leave stage': 5, 'taking photos': 75}
4
{'one': 10, 'five': 60, 'nine': 5, 'four': 10, 'three': 15}
{'one': 5, 'five': 10, 'nine': 0, 'four': 30, 'three': 55}
{'one': 20, 'five': 10, 'nine': 5, 'four': 15, 'three': 50}
4
{'pull the dog away': 10, 'touch the girl': 20, 'raise her hands': 40, 'sit next to child again': 15, 'sit down': 15}
{'pull the dog away': 5, 'touch the girl': 10, 'raise her hands': 25, 'sit next to child again': 5, 'sit down': 10}
{'pull the dog away': 5, 'touch the girl': 5, 'raise her hands': 10, 'sit next to child again': 10, 'sit down': 70}
2
{'dance': 5, 'cycle away': 1, 'pull rope': 1, 'lights on the stage blink': 80, 'stand up': 13}
{'dance': 5, 'cycle away': 5, 'pull rope': 5, 'lights on the stage blink': 15, 'stand up': 70}
{'dance': 5, 'cycle away': 5, 'pull rope': 5, 'lights on the stage blink': 10, 'stand up': 75}
3
{'eight': 30, 'four': 40, 'six': 25, 'one': 2, 'three': 3}
{'eight': 5, 'four': 70, 'six': 5, 'one': 10, 'three': 10}
{'eight': 0, 'four': 0, 'six': 0, 'one': 0, 'three': 100}
1
{'feed smaller owl': 10, 'puts his hand on the baby': 5, 'continue walking': 5, 'move up': 60, 'continue eating': 20}
{'feed smaller owl': 10, 'puts his hand on the baby': 5, 'continue walking': 5, 'move up': 20, 'continue eating': 60}
{'feed smaller owl': 20, 'puts his hand on the baby': 0, 'continue walking': 5, 'move up': 5, 'continue eating': 5}
0
{'suggest taking the food away': 5, 'the baby is angry': 5, 'answering cameraman s question': 10, 'ask for permission': 80, 'to ask for milk': 0}
{'suggest taking the food away': 10, 'the baby is angry': 5, 'answering cameraman s question': 60, 'ask for permission': 20, 'to ask for milk': 5}
{'suggest taking the food away': 10, 'the baby is angry': 5, 'answering cameraman s question': 30, 'ask for permission': 70, 'to ask for milk': 5}
3
{'hug the dog': 10, 'plays with her': 5, 'turn towards lady': 70, 'turn back and run': 5, 'try to lick her face': 10}
{'hug the dog': 10, 'plays with her': 15, 'turn towards lady': 60, 'turn back and run': 5, 'try to lick her face': 10}
{'hug the dog': 5, 'plays with her': 5, 'turn towards lady': 30, 'turn back and run': 55, 'try to lick her face': 5}
3
{'taking photos': 5, 'observe': 15, 'kick forwards': 5, 'drinking bottle': 5, 'dancing': 70}
{'taking photos': 5, 'observe': 85, 'kick forwards': 0, 'drinking bottle': 5, 'dancing': 5}
{'taking photos': 5, 'observe': 90, 'kick forwards': 0, 'drinking bottle': 5, 'dancing': 0}
1
{'drink': 10, 'look to his left': 25, 'smiled': 50, 'look backwards': 15, 'walk away': 30}
{'drink': 5, 'look to his left': 40, 'smiled': 10, 'look backwards': 15, 'walk away': 10}
{'drink': 5, 'look to his left': 10, 'smiled': 5, 'look backwards': 10, 'walk away': 70}
4
{'seven': 25, 'one': 5, 'two': 10, 'six': 30, 'four': 30}
{'seven': 40, 'one': 5, 'two': 5, 'six': 40, 'four': 10}
{'seven': 70, 'six': 15, 'four': 10, 'two': 3, 'one': 2}
3
{'move pebbles': 10, 'lie on his back': 10, 'walk away': 30, 'take taco up': 15, 'point to camera': 15}
{'move pebbles': 5, 'lie on his back': 70, 'walk away': 10, 'take taco up': 5, 'point to camera': 10}
{'move pebbles': 0, 'lie on his back': 90, 'walk away': 5, 'take taco up': 0, 'point to camera': 5}
1
{'asking a question': 10, 'announcing the winner': 70, 'stretching': 5, 'wanted to hit someone': 5, 'dancing': 10}
{'asking a question': 60, 'announcing the winner': 25, 'stretching': 5, 'wanted to hit someone': 2, 'dancing': 8}
{'asking a question': 20, 'announcing the winner': 70, 'stretching': 5, 'wanted to hit someone': 1, 'dancing': 4}
1
{'seven': 70, 'eleven': 5, 'two': 3, 'six': 7, 'eight': 5}
{'seven': 20, 'eleven': 5, 'two': 5, 'six': 30, 'eight': 40}
{'seven': 70, 'eleven': 5, 'two': 10, 'six': 10, 'eight': 5}
4
{'put his foot down': 70, 'raising out his arms': 15, 'with a rope': 0, 'spread legs and arms out': 10, 'jump down': 30}
{'put his foot down': 30, 'raising out his arms': 15, 'with a rope': 0, 'spread legs and arms out': 50, 'jump down': 25}
{'put his foot down': 10, 'raising out his arms': 15, 'with a rope': 0, 'spread legs and arms out': 20, 'jump down': 55}
4
{'cross one leg over the other': 20, 'touch baby s foot': 5, 'playing with sofa': 5, 'dance': 5, 'cross her arms': 10}
{'cross one leg over the other': 5, 'touch baby s foot': 0, 'playing with sofa': 30, 'dance': 0, 'cross her arms': 5}
{'cross one leg over the other': 5, 'touch baby s foot': 5, 'playing with sofa': 80, 'dance': 5, 'cross her arms': 5}
2
{'release her from the rope': 5, 'play with sand': 5, 'a flip': 20, 'calling for doctor': 5, 'shaking pompoms': 5}
{'release her from the rope': 5, 'play with sand': 1, 'a flip': 20, 'calling for doctor': 5, 'shaking pompoms': 15}
{'release her from the rope': 5, 'play with sand': 60, 'a flip': 10, 'calling for doctor': 5, 'shaking pompoms': 20}
2
{'bend down to pick it': 60, 'lift up her shirt': 5, 'get up and continue dancing': 10, 'touch the baby s arm': 5, 'sits down': 20}
{'bend down to pick it': 5, 'lift up her shirt': 2, 'get up and continue dancing': 3, 'touch the baby s arm': 15, 'sits down': 20}
{'bend down to pick it': 5, 'lift up her shirt': 1, 'get up and continue dancing': 2, 'touch the baby s arm': 20, 'sits down': 10}
4
{'kiss him': 5, 'hand over the toy': 5, 'hold his hands': 80, 'open the box': 5, 'hug the boy': 5}
{'kiss him': 20, 'hand over the toy': 10, 'hold his hands': 50, 'open the box': 5, 'hug the boy': 30}
{'kiss him': 0, 'hand over the toy': 95, 'hold his hands': 5, 'open the box': 0, 'hug the boy': 0}
1
{'hug dog': 10, 'wagging tail': 20, 'pick up the toy': 5, 'jumped': 60, 'supported the puppy': 5}
{'hug dog': 5, 'wagging tail': 20, 'pick up the toy': 5, 'jumped': 15, 'supported the puppy': 5}
{'hug dog': 5, 'wagging tail': 5, 'pick up the toy': 5, 'jumped': 15, 'supported the puppy': 5}
3
{'coworkers': 10, 'team member': 15, 'rock': 0, 'work mates': 10, 'friends': 90}
{'coworkers': 40, 'team member': 85, 'rock': 10, 'work mates': 35, 'friends': 60}
{'coworkers': 40, 'team member': 80, 'rock': 5, 'work mates': 40, 'friends': 30}
4
{'continue bouncing up and down': 10, 'stand at the side and watch': 30, 'blow out candles': 0, 'push the boy': 55, 'stand up': 5}
{'continue bouncing up and down': 10, 'stand at the side and watch': 70, 'blow out candles': 0, 'push the boy': 15, 'stand up': 5}
{'continue bouncing up and down': 10, 'stand at the side and watch': 20, 'blow out candles': 0, 'push the boy': 70, 'stand up': 10}
3
{'seven': 5, 'two': 30, 'three': 60, 'five': 3, 'eight': 2}
{'seven': 5, 'two': 30, 'three': 50, 'five': 15, 'eight': 0}
{'seven': 10, 'two': 5, 'three': 10, 'five': 70, 'eight': 5}
3
{'eleven': 0, 'two': 90, 'four': 5, 'six': 0, 'one': 5}
{'eleven': 1, 'two': 10, 'four': 2, 'six': 1, 'one': 86}
{'eleven': 0, 'two': 5, 'four': 0, 'six': 0, 'one': 95}
4
{'three': 5, 'six': 70, 'nine': 5, 'two': 5, 'four': 15}
{'three': 0, 'six': 0, 'nine': 100, 'two': 0, 'four': 0}
{'three': 10, 'six': 25, 'nine': 60, 'two': 5, 'four': 10}
2
{'withdrew toy': 40, 'shake his body': 10, 'blow kisses': 50, 'pat the chair': 45, 'shake hands': 15}
{'withdrew toy': 60, 'shake his body': 10, 'blow kisses': 10, 'pat the chair': 10, 'shake hands': 10}
{'withdrew toy': 90, 'shake his body': 2, 'blow kisses': 2, 'pat the chair': 3, 'shake hands': 3}
0
{'play flute': 10, 'watching her': 60, 'raise his arms': 5, 'observe': 55, 'his surroundings': 30}
{'play flute': 60, 'watching her': 20, 'raise his arms': 5, 'observe': 10, 'his surroundings': 5}
{'play flute': 90, 'watching her': 5, 'raise his arms': 1, 'observe': 2, 'his surroundings': 2}
0
{'lure the dog to jump': 60, 'performing': 5, 'playing the piano': 0, 'talking': 10, 'direct attention': 85}
{'lure the dog to jump': 70, 'performing': 5, 'playing the piano': 0, 'talking': 15, 'direct attention': 60}
{'lure the dog to jump': 90, 'performing': 5, 'playing the piano': 0, 'talking': 3, 'direct attention': 2}
0
{'her finger': 20, 'multicolor box': 5, 'pacifier': 5, 'food': 65, 'cat toy': 5}
{'her finger': 10, 'multicolor box': 5, 'pacifier': 5, 'food': 80, 'cat toy': 0}
{'her finger': 10, 'multicolor box': 5, 'pacifier': 70, 'food': 10, 'cat toy': 5}
2
{'likes it': 70, 'excited': 10, 'disappointed': 5, 'bored': 15, 'sad': 0}
{'likes it': 5, 'excited': 5, 'disappointed': 40, 'bored': 45, 'sad': 20}
{'likes it': 20, 'excited': 40, 'disappointed': 15, 'bored': 15, 'sad': 10}
1
{'piercing': 5, 'necklace': 0, 'bandana': 0, 'glasses': 0, 'fake mustache': 95}
{'piercing': 5, 'necklace': 1, 'bandana': 2, 'glasses': 90, 'fake mustache': 2}
{'piercing': 5, 'necklace': 5, 'bandana': 5, 'glasses': 10, 'fake mustache': 30}
4
{'to check the water level': 0, 'wear it for girl': 5, 'sell': 0, 'introduce it': 10, 'to play with baby': 85}
{'to check the water level': 5, 'wear it for girl': 10, 'sell': 5, 'introduce it': 40, 'to play with baby': 40}
{'to check the water level': 0, 'wear it for girl': 0, 'sell': 0, 'introduce it': 10, 'to play with baby': 90}
4
{'stage': 20, 'ball room': 5, 'by a lake': 10, 'carnival': 60, 'room': 5}
{'stage': 90, 'ball room': 5, 'by a lake': 0, 'carnival': 3, 'room': 2}
{'stage': 90, 'ball room': 5, 'by a lake': 0, 'carnival': 10, 'room': 5}
3
{'eight': 0, 'five': 0, 'four': 0, 'one': 20, 'two': 80}
{'eight': 0, 'five': 0, 'four': 0, 'one': 95, 'two': 5}
{'eight': 0, 'five': 0, 'four': 0, 'one': 95, 'two': 5}
3
{'perch on sofa arm': 60, 'place on shoulder': 5, 'place on the cat': 5, 'on his laps': 10, 'sit on hands': 5}
{'perch on sofa arm': 10, 'place on shoulder': 5, 'place on the cat': 0, 'on his laps': 70, 'sit on hands': 15}
{'perch on sofa arm': 80, 'place on shoulder': 5, 'place on the cat': 0, 'on his laps': 10, 'sit on hands': 5}
0
{'rest his hands': 35, 'focus on laptop': 25, 'gave the microphone back': 20, 'picked up his bottle': 15, 'look down and shake head': 5}
{'focus on laptop': 10, 'look down and shake head': 5, 'gave the microphone back': 60, 'rest his hands': 15, 'picked up his bottle': 10}
{'focus on laptop': 5, 'look down and shake head': 5, 'gave the microphone back': 5, 'rest his hands': 80, 'picked up his bottle': 5}
3
{'jumping': 20, 'eating': 5, 'watching television': 5, 'reading a book': 5, 'sleeping': 15}
{'jumping': 1, 'eating': 2, 'watching television': 10, 'reading a book': 1, 'sleeping': 1}
{'jumping': 95, 'eating': 1, 'watching television': 1, 'reading a book': 1, 'sleeping': 2}
0
{'green': 60, 'light blue': 10, 'black': 25, 'pink': 2, 'white': 3}
{'green': 0, 'light blue': 0, 'black': 95, 'pink': 0, 'white': 5}
{'green': 5, 'light blue': 5, 'black': 85, 'pink': 3, 'white': 2}
2
{'bar': 30, 'field': 0, 'barren land': 0, 'event room': 60, 'lake side': 0}
{'bar': 70, 'field': 5, 'barren land': 1, 'event room': 20, 'lake side': 4}
{'bar': 20, 'field': 5, 'barren land': 0, 'event room': 75, 'lake side': 0}
3
{'enjoy skiing': 10, 'engage the audience': 20, 'successfully hit the ball': 10, 'prevent wind stinging eyes': 5, 'taking photo with baby shark': 55}
{'enjoy skiing': 10, 'engage the audience': 30, 'successfully hit the ball': 15, 'prevent wind stinging eyes': 5, 'taking photo with baby shark': 5}
{'enjoy skiing': 5, 'engage the audience': 30, 'successfully hit the ball': 5, 'prevent wind stinging eyes': 5, 'taking photo with baby shark': 5}
4
{'jungle': 0, 'speech event': 10, 'stage': 30, 'classroom': 55, 'park': 5}
{'jungle': 0, 'speech event': 20, 'stage': 10, 'classroom': 70, 'park': 0}
{'jungle': 5, 'speech event': 80, 'stage': 10, 'classroom': 40, 'park': 5}
3
{'house': 5, 'petting zoo': 40, 'archery practice': 40, 'carpark': 5, 'museum': 10}
{'house': 5, 'petting zoo': 5, 'archery practice': 85, 'carpark': 3, 'museum': 2}
{'house': 0, 'petting zoo': 0, 'archery practice': 95, 'carpark': 0, 'museum': 0}
2
{'in the day': 10, 'house': 30, 'hiking': 15, 'living room': 20, 'presentation hall': 25}
{'in the day': 10, 'house': 5, 'hiking': 0, 'living room': 5, 'presentation hall': 80}
{'in the day': 5, 'house': 0, 'hiking': 0, 'living room': 0, 'presentation hall': 95}
4
{'keeps it in his pocket': 30, 'walk': 0, 'pet dog': 5, 'take off helmet': 5, 'wipe his mouth': 60}
{'keeps it in his pocket': 30, 'walk': 10, 'pet dog': 20, 'take off helmet': 5, 'wipe his mouth': 35}
{'keeps it in his pocket': 5, 'walk': 20, 'pet dog': 70, 'take off helmet': 0, 'wipe his mouth': 5}
2
{'three': 35, 'four': 45, 'one': 5, 'two': 10, 'nine': 5}
{'three': 35, 'four': 45, 'one': 5, 'two': 10, 'nine': 5}
{'three': 70, 'two': 20, 'one': 5, 'four': 3, 'nine': 2}
1
{'follow the tv': 20, 'passing to man to help': 15, 'observe the keyboard': 5, 'reach for girl in red': 10, 'looking for something': 30}
{'follow the tv': 10, 'passing to man to help': 40, 'observe the keyboard': 15, 'reach for girl in red': 15, 'looking for something': 30}
{'follow the tv': 5, 'passing to man to help': 80, 'observe the keyboard': 5, 'reach for girl in red': 5, 'looking for something': 5}
1
{'three': 30, 'six': 5, 'four': 45, 'two': 20, 'five': 0}
{'three': 60, 'two': 30, 'four': 5, 'five': 3, 'six': 2}
{'three': 95, 'six': 1, 'four': 1, 'two': 2, 'five': 1}
0
{'kissed him': 10, 'adjust the baby s shirt': 5, 'shake her legs': 0, 'smiling': 20, 'looks worried': 40}
{'kissed him': 5, 'adjust the baby s shirt': 5, 'shake her legs': 0, 'smiling': 85, 'looks worried': 20}
{'kissed him': 5, 'adjust the baby s shirt': 5, 'shake her legs': 1, 'smiling': 85, 'looks worried': 4}
3
{'outdoors': 85, 'bedroom': 0, 'snowy hill': 95, 'stage': 0, 'studio': 0}
{'outdoors': 90, 'bedroom': 0, 'snowy hill': 85, 'stage': 0, 'studio': 0}
{'outdoors': 85, 'bedroom': 0, 'snowy hill': 95, 'stage': 0, 'studio': 0}
2
{'three': 15, 'one': 5, 'four': 10, 'two': 65, 'six': 5}
{'three': 5, 'one': 85, 'four': 3, 'two': 7, 'six': 0}
{'three': 5, 'one': 85, 'four': 5, 'two': 5, 'six': 0}
1
{'drink something': 10, 'posing': 15, 'smile': 50, 'talk to lady': 40, 'pointed to his front': 20}
{'drink something': 10, 'posing': 40, 'smile': 80, 'talk to lady': 75, 'pointed to his front': 5}
{'drink something': 5, 'posing': 5, 'smile': 10, 'talk to lady': 80, 'pointed to his front': 0}
2
{'stare curiously': 40, 'bouncing': 5, 'swing legs': 5, 'move his arms': 90, 'play with toy': 10}
{'stare curiously': 70, 'bouncing': 5, 'swing legs': 5, 'move his arms': 10, 'play with toy': 10}
{'stare curiously': 40, 'bouncing': 5, 'swing legs': 5, 'move his arms': 90, 'play with toy': 10}
3
{'moves around': 10, 'walked away': 5, 'move head to the beat': 60, 'pays guitar': 0, 'talk to him': 5}
{'moves around': 40, 'walked away': 10, 'move head to the beat': 60, 'pays guitar': 50, 'talk to him': 20}
{'moves around': 10, 'walked away': 5, 'move head to the beat': 15, 'pays guitar': 0, 'talk to him': 70}
2
{'cover his face': 0, 'slipped and fell': 0, 'got a shock': 0, 'knocked down': 0, 'lost balance': 0}
{'cover his face': 5, 'slipped and fell': 20, 'got a shock': 5, 'knocked down': 5, 'lost balance': 65}
{'cover his face': 5, 'slipped and fell': 10, 'got a shock': 5, 'knocked down': 5, 'lost balance': 75}
4
{'swimming pool': 5, 'garden': 40, 'living room': 30, 'trail': 20, 'on the road': 5}
{'swimming pool': 5, 'garden': 5, 'living room': 20, 'trail': 5, 'on the road': 5}
{'swimming pool': 5, 'garden': 5, 'living room': 5, 'trail': 5, 'on the road': 10}
2
{'buying drink': 5, 'shake the bottle': 10, 'feeding dogs': 0, 'touch baby': 0, 'take own cup': 85}
{'buying drink': 5, 'shake the bottle': 10, 'feeding dogs': 0, 'touch baby': 0, 'take own cup': 15}
{'buying drink': 5, 'shake the bottle': 15, 'feeding dogs': 0, 'touch baby': 0, 'take own cup': 0}
1
{'watching the man write calligraphy': 10, 'need to play the drum': 5, 'open space': 15, 'looking after the child': 10, 'to show to people': 20}
{'watching the man write calligraphy': 5, 'need to play the drum': 5, 'open space': 10, 'looking after the child': 5, 'to show to people': 20}
{'watching the man write calligraphy': 5, 'need to play the drum': 5, 'open space': 10, 'looking after the child': 80, 'to show to people': 0}
3
{'five': 0, 'three': 95, 'two': 2, 'one': 1, 'four': 2}
{'five': 5, 'three': 10, 'two': 75, 'one': 5, 'four': 5}
{'five': 5, 'three': 20, 'two': 70, 'one': 3, 'four': 2}
1
{'birthday': 80, 'for more servings to share': 5, 'girl s birthday': 90, 'gifts for woman in black': 0, 'boy s birthday': 5}
{'birthday': 85, 'for more servings to share': 5, 'girl s birthday': 50, 'gifts for woman in black': 0, 'boy s birthday': 40}
{'birthday': 70, 'for more servings to share': 5, 'girl s birthday': 90, 'gifts for woman in black': 0, 'boy s birthday': 5}
2
{'girl pressed button': 5, 'called for help': 5, 'automatically': 5, 'opening the lid': 5, 'tearing a piece out': 5}
{'girl pressed button': 5, 'called for help': 5, 'automatically': 10, 'opening the lid': 70, 'tearing a piece out': 10}
{'girl pressed button': 5, 'called for help': 5, 'automatically': 5, 'opening the lid': 85, 'tearing a piece out': 0}
3
{'under the bed': 85, 'behind the sofa': 5, 'behind the drawer': 3, 'on the bed': 4, 'in the kitchen': 3}
{'under the bed': 15, 'behind the sofa': 10, 'behind the drawer': 20, 'on the bed': 15, 'in the kitchen': 25}
{'under the bed': 70, 'behind the sofa': 5, 'behind the drawer': 5, 'on the bed': 10, 'in the kitchen': 10}
0
{'take video': 10, 'watching the performance': 10, 'training': 40, 'catch ball': 5, 'jump off platform': 5}
{'take video': 5, 'watching the performance': 5, 'training': 20, 'catch ball': 5, 'jump off platform': 65}
{'take video': 5, 'watching the performance': 10, 'training': 80, 'catch ball': 0, 'jump off platform': 5}
4
{'residential area': 90, 'hiking': 2, 'park': 2, 'in the sea': 2, 'in the desert': 4}
{'residential area': 5, 'hiking': 5, 'park': 5, 'in the sea': 5, 'in the desert': 5}
{'residential area': 5, 'hiking': 5, 'park': 5, 'in the sea': 5, 'in the desert': 10}
0
{'turning it': 40, 'clap hands': 10, 'paused to look at the hole': 20, 'grabs the lady': 5, 'enters the toy car': 25}
{'turning it': 20, 'clap hands': 5, 'paused to look at the hole': 10, 'grabs the lady': 5, 'enters the toy car': 15}
{'turning it': 5, 'clap hands': 5, 'paused to look at the hole': 5, 'grabs the lady': 5, 'enters the toy car': 80}
0
{'two': 20, 'six': 5, 'four': 15, 'eleven': 0, 'five': 60}
{'two': 70, 'six': 5, 'four': 10, 'eleven': 0, 'five': 15}
{'two': 90, 'six': 2, 'four': 3, 'eleven': 1, 'five': 4}
0
{'parked': 30, 'road block': 5, 'ran out of petrol': 5, 'red traffic light': 10, 'drop-off the children': 50}
{'parked': 80, 'road block': 5, 'ran out of petrol': 5, 'red traffic light': 5, 'drop-off the children': 20}
{'parked': 10, 'road block': 5, 'ran out of petrol': 5, 'red traffic light': 5, 'drop-off the children': 75}
0
{'point at toy cars': 5, 'put on seat belt': 5, 'dance': 5, 'wave': 80, 'hold her phone': 5}
{'point at toy cars': 5, 'put on seat belt': 10, 'dance': 5, 'wave': 10, 'hold her phone': 10}
{'point at toy cars': 5, 'put on seat belt': 10, 'dance': 5, 'wave': 80, 'hold her phone': 0}
3
{'stands up and run towards the man': 5, 'speak to microphone': 0, 'take the food': 0, 'feed baby': 0, 'run away': 10}
{'stands up and run towards the man': 5, 'speak to microphone': 1, 'take the food': 2, 'feed baby': 1, 'run away': 10}
{'stands up and run towards the man': 5, 'speak to microphone': 0, 'take the food': 40, 'feed baby': 5, 'run away': 10}
4
{'part of the attire': 20, 'ride motorcycle': 0, 'sunny weather': 70, 'keep warm': 10, 'working at great height': 0}
{'part of the attire': 70, 'ride motorcycle': 5, 'sunny weather': 50, 'keep warm': 40, 'working at great height': 2}
{'part of the attire': 40, 'ride motorcycle': 0, 'sunny weather': 10, 'keep warm': 90, 'working at great height': 0}
3
{'stablise himself': 40, 'paddle': 35, 'fall down': 10, 'shake hands': 5, 'stand up': 10}
{'stablise himself': 60, 'paddle': 10, 'fall down': 20, 'shake hands': 5, 'stand up': 40}
{'stablise himself': 40, 'paddle': 5, 'fall down': 5, 'shake hands': 0, 'stand up': 50}
0
{'dancing': 5, 'singing': 5, 'look at man': 85, 'talked to the camera': 3, 'pat his shoulder': 2}
{'dancing': 5, 'singing': 5, 'look at man': 20, 'talked to the camera': 70, 'pat his shoulder': 0}
{'dancing': 5, 'singing': 5, 'look at man': 70, 'talked to the camera': 15, 'pat his shoulder': 5}
3
{'close in her arms': 70, 'in left arm supporting baby s head': 50, 'spoon': 0, 'squat': 5, 'hold her hand on the can': 0}
{'close in her arms': 20, 'in left arm supporting baby s head': 60, 'spoon': 0, 'squat': 0, 'hold her hand on the can': 5}
{'close in her arms': 30, 'in left arm supporting baby s head': 90, 'spoon': 0, 'squat': 0, 'hold her hand on the can': 0}
0
{'snow mountain': 5, 'zoo': 5, 'swimming pool': 10, 'bedroom': 60, 'beach': 5}
{'snow mountain': 10, 'zoo': 5, 'swimming pool': 25, 'bedroom': 5, 'beach': 30}
{'snow mountain': 5, 'zoo': 5, 'swimming pool': 15, 'bedroom': 5, 'beach': 5}
3
{'walk away from the table': 50, 'clap her hands': 10, 'talk to the audience': 30, 'touch man s head': 5, 'run to camera': 5}
{'walk away from the table': 5, 'clap her hands': 15, 'talk to the audience': 20, 'touch man s head': 30, 'run to camera': 10}
{'walk away from the table': 5, 'clap her hands': 10, 'talk to the audience': 70, 'touch man s head': 5, 'run to camera': 10}
3
{"pat the dog's head": 70, 'gave dog food': 5, 'rubbed its neck': 40, 'caress': 65, 'holds the dog': 30}
{"pat the dog's head": 40, 'gave dog food': 5, 'rubbed its neck': 30, 'caress': 50, 'holds the dog': 25}
{"pat the dog's head": 5, 'gave dog food': 5, 'rubbed its neck': 30, 'caress': 5, 'holds the dog': 5}
3
{'fidgeting': 60, 'relaxing': 20, 'rolling around': 10, 'exercise': 5, 'looking at camera': 5}
{'fidgeting': 30, 'relaxing': 70, 'rolling around': 5, 'exercise': 0, 'looking at camera': 10}
{'fidgeting': 85, 'relaxing': 10, 'rolling around': 2, 'exercise': 1, 'looking at camera': 2}
0
{'white': 5, 'green': 1, 'silver': 1, 'black': 10, 'blue': 83}
{'white': 5, 'green': 1, 'silver': 1, 'black': 60, 'blue': 33}
{'white': 0, 'green': 0, 'silver': 0, 'black': 95, 'blue': 5}
3
{'two': 40, 'nine': 0, 'one': 5, 'four': 5, 'three': 50}
{'two': 30, 'nine': 0, 'one': 20, 'four': 10, 'three': 40}
{'two': 85, 'one': 10, 'three': 3, 'four': 1, 'nine': 1}
0
{'car': 5, 'plank': 60, 'bicycle': 10, 'motorcycle': 5, 'paddles': 5}
{'car': 10, 'plank': 5, 'bicycle': 5, 'motorcycle': 5, 'paddles': 0}
{'car': 5, 'plank': 85, 'bicycle': 5, 'motorcycle': 3, 'paddles': 2}
1
{'feed baby': 5, 'reach for the airconditioners': 1, 'look at camera': 10, 'stretch out his hands': 3, 'sit down': 2}
{'feed baby': 5, 'reach for the airconditioners': 0, 'look at camera': 10, 'stretch out his hands': 75, 'sit down': 10}
{'feed baby': 5, 'reach for the airconditioners': 0, 'look at camera': 85, 'stretch out his hands': 5, 'sit down': 5}
2
{'one': 40, 'three': 0, 'four': 0, 'two': 60, 'nine': 0}
{'one': 40, 'two': 50, 'three': 5, 'four': 3, 'nine': 2}
{'one': 0, 'three': 100, 'four': 0, 'two': 0, 'nine': 0}
1
{'walk': 70, 'sniffing the man': 15, 'push dog': 5, 'about to go out': 5, 'wag tail': 5}
{'walk': 10, 'sniffing the man': 40, 'push dog': 5, 'about to go out': 10, 'wag tail': 35}
{'walk': 40, 'sniffing the man': 50, 'push dog': 5, 'about to go out': 5, 'wag tail': 20}
1
{'climbed higher and further': 5, 'restricted environment': 70, 'cant go nearby': 80, 'trying to land': 30, 'prevent getting washed away': 5}
{'climbed higher and further': 10, 'restricted environment': 50, 'cant go nearby': 40, 'trying to land': 20, 'prevent getting washed away': 5}
{'climbed higher and further': 5, 'restricted environment': 30, 'cant go nearby': 80, 'trying to land': 10, 'prevent getting washed away': 0}
2
{'fetch the toy': 10, 'drop toy': 10, 'put dog back': 5, 'step back': 5, 'kiss the dog': 70}
{'fetch the toy': 5, 'drop toy': 5, 'put dog back': 10, 'step back': 10, 'kiss the dog': 20}
{'fetch the toy': 5, 'drop toy': 5, 'put dog back': 80, 'step back': 5, 'kiss the dog': 5}
4
{'reject the lady': 10, 'show gesture': 60, 'angry with the lady': 10, 'want to push her': 5, 'agreeing with lady': 15}
{'reject the lady': 5, 'show gesture': 40, 'angry with the lady': 5, 'want to push her': 0, 'agreeing with lady': 50}
{'reject the lady': 5, 'show gesture': 10, 'angry with the lady': 0, 'want to push her': 0, 'agreeing with lady': 85}
4
{'bring to the person': 40, 'touch brown dog s paw': 5, 'sits down': 20, 'tries to bite it': 5, 'run back to man': 30}
{'bring to the person': 10, 'touch brown dog s paw': 25, 'sits down': 40, 'tries to bite it': 20, 'run back to man': 5}
{'bring to the person': 5, 'touch brown dog s paw': 70, 'sits down': 10, 'tries to bite it': 5, 'run back to man': 10}
1
{'lie prone on back': 5, 'sitting on baby chair': 70, 'roughly': 20, 'baby stroller': 0, 'crawl': 5}
{'lie prone on back': 0, 'sitting on baby chair': 0, 'roughly': 20, 'baby stroller': 0, 'crawl': 0}
{'lie prone on back': 0, 'sitting on baby chair': 0, 'roughly': 20, 'baby stroller': 0, 'crawl': 0}
2
{'three': 5, 'four': 5, 'nine': 5, 'six': 5, 'one': 20}
{'one': 5, 'three': 10, 'four': 20, 'six': 35, 'nine': 30}
{'three': 1, 'four': 1, 'nine': 1, 'six': 1, 'one': 96}
4
{'no reaction': 5, 'made hand gestures': 45, 'walked away': 5, 'shouted at baby': 45, 'rock on the chair': 0}
{'no reaction': 80, 'made hand gestures': 5, 'walked away': 5, 'shouted at baby': 5, 'rock on the chair': 5}
{'no reaction': 80, 'made hand gestures': 10, 'walked away': 5, 'shouted at baby': 3, 'rock on the chair': 2}
0
{'holding the baby in her hands': 80, 'laugh': 40, 'walk to the man': 10, 'hold baby s body': 75, 'hit water with hand': 15}
{'holding the baby in her hands': 10, 'laugh': 80, 'walk to the man': 5, 'hold baby s body': 10, 'hit water with hand': 15}
{'holding the baby in her hands': 30, 'laugh': 80, 'walk to the man': 5, 'hold baby s body': 50, 'hit water with hand': 5}
1
{'in the living room': 45, 'indoor': 25, 'concert stage': 5, 'living room': 25, 'concert hall': 0}
{'in the living room': 60, 'indoor': 80, 'concert stage': 5, 'living room': 60, 'concert hall': 5}
{'in the living room': 70, 'indoor': 50, 'concert stage': 5, 'living room': 70, 'concert hall': 5}
1
{'four': 5, 'two': 60, 'five': 5, 'one': 15, 'three': 15}
{'four': 5, 'two': 25, 'five': 2, 'one': 30, 'three': 38}
{'four': 5, 'two': 85, 'five': 2, 'one': 3, 'three': 5}
4
{'look around nervously': 40, 'raise hands in the air': 60, 'smile': 5, 'sways and play': 5, 'turns her towards him': 90}
{'look around nervously': 30, 'raise hands in the air': 15, 'smile': 20, 'sways and play': 5, 'turns her towards him': 30}
{'look around nervously': 1, 'raise hands in the air': 1, 'smile': 5, 'sways and play': 1, 'turns her towards him': 1}
2
{'touch baby s nose': 20, 'hold baby s stomach': 5, 'kiss baby': 70, 'push the chair baby is in': 0, 'kiss its forehead': 85}
{'touch baby s nose': 20, 'hold baby s stomach': 30, 'kiss baby': 50, 'push the chair baby is in': 0, 'kiss its forehead': 60}
{'touch baby s nose': 10, 'hold baby s stomach': 10, 'kiss baby': 70, 'push the chair baby is in': 5, 'kiss its forehead': 40}
2
{'hold hands': 5, 'by hand movements': 5, 'make eye contact everywhere': 10, 'spectacles': 5, 'follow the children': 15}
{'hold hands': 10, 'by hand movements': 5, 'make eye contact everywhere': 5, 'spectacles': 0, 'follow the children': 80}
{'hold hands': 10, 'by hand movements': 10, 'make eye contact everywhere': 10, 'spectacles': 70, 'follow the children': 10}
3
{'lie on sofa': 5, 'pose for photo': 50, 'looks forward': 30, 'turn away': 10, 'tries to say something': 15}
{'lie on sofa': 5, 'pose for photo': 40, 'looks forward': 35, 'turn away': 10, 'tries to say something': 10}
{'lie on sofa': 5, 'pose for photo': 10, 'looks forward': 20, 'turn away': 65, 'tries to say something': 0}
3
{'talk to the lady': 10, 'kick his foot': 10, 'drink': 5, 'point fingers towards the girl': 10, 'takes his teddy bear': 65}
{'talk to the lady': 10, 'kick his foot': 5, 'drink': 10, 'point fingers towards the girl': 5, 'takes his teddy bear': 2}
{'talk to the lady': 5, 'kick his foot': 5, 'drink': 20, 'point fingers towards the girl': 5, 'takes his teddy bear': 5}
2
{'pick up shoe': 5, 'point at the bicycle': 5, 'kiss boy': 20, 'hold her hands': 50, 'look at her hands': 20}
{'pick up shoe': 5, 'point at the bicycle': 2, 'kiss boy': 20, 'hold her hands': 25, 'look at her hands': 10}
{'pick up shoe': 5, 'point at the bicycle': 5, 'kiss boy': 80, 'hold her hands': 5, 'look at her hands': 5}
2
{'three': 25, 'two': 60, 'five': 0, 'four': 0, 'one': 15}
{'three': 60, 'two': 30, 'five': 5, 'four': 3, 'one': 2}
{'three': 90, 'two': 7, 'five': 1, 'four': 1, 'one': 1}
0
{'unable to pay attention': 5, 'tired': 5, 'shy and nervous': 5, 'keep his hair in check': 5, 'heard a funny joke': 5}
{'unable to pay attention': 10, 'tired': 10, 'shy and nervous': 60, 'keep his hair in check': 5, 'heard a funny joke': 15}
{'unable to pay attention': 10, 'tired': 10, 'shy and nervous': 15, 'keep his hair in check': 60, 'heard a funny joke': 5}
2
{'turns the frame around': 5, 'start clapping': 5, 'use phone': 10, 'hug herself': 5, 'sit down': 20}
{'turns the frame around': 60, 'start clapping': 10, 'use phone': 10, 'hug herself': 10, 'sit down': 10}
{'turns the frame around': 5, 'start clapping': 5, 'use phone': 80, 'hug herself': 5, 'sit down': 5}
2
{'three': 35, 'six': 10, 'eight': 5, 'five': 30, 'one': 20}
{'one': 40, 'three': 30, 'five': 15, 'six': 10, 'eight': 5}
{'three': 10, 'six': 10, 'eight': 5, 'five': 70, 'one': 5}
0
{'started barking and moving hands': 5, 'moves away': 85, 'follow white dog': 0, 'run to the brown dog': 5, 'jump up': 5}
{'started barking and moving hands': 5, 'moves away': 25, 'follow white dog': 10, 'run to the brown dog': 0, 'jump up': 60}
{'started barking and moving hands': 0, 'moves away': 90, 'follow white dog': 10, 'run to the brown dog': 0, 'jump up': 0}
4
{'look up smile and move hand': 50, 'feeding the dog': 5, 'shake hands': 10, 'touch it': 30, 'eating': 5}
{'look up smile and move hand': 15, 'feeding the dog': 0, 'shake hands': 5, 'touch it': 50, 'eating': 30}
{'look up smile and move hand': 10, 'feeding the dog': 0, 'shake hands': 70, 'touch it': 20, 'eating': 0}
2
{'in house': 70, 'stage': 20, 'carnival': 2, 'outdoors': 3, 'park': 5}
{'in house': 30, 'stage': 80, 'carnival': 5, 'outdoors': 10, 'park': 5}
{'in house': 20, 'stage': 75, 'carnival': 2, 'outdoors': 1, 'park': 2}
1
{'colleagues': 0, 'birthday': 0, 'the camera': 0, 'balloon': 0, 'birthday celebration': 0}
{'colleagues': 5, 'birthday': 5, 'the camera': 85, 'balloon': 5, 'birthday celebration': 5}
{'colleagues': 0, 'birthday': 0, 'the camera': 20, 'balloon': 0, 'birthday celebration': 0}
2
{'lick': 60, 'with two hands': 10, 'pick it up': 40, 'wave spoon around': 5, 'use spoon with the fork': 0}
{'lick': 70, 'with two hands': 5, 'pick it up': 10, 'wave spoon around': 15, 'use spoon with the fork': 0}
{'lick': 5, 'with two hands': 5, 'pick it up': 10, 'wave spoon around': 80, 'use spoon with the fork': 0}
0
{'happy': 90, 'tired': 2, 'angry': 1, 'alert': 5, 'reluctant': 2}
{'happy': 70, 'tired': 40, 'angry': 5, 'alert': 60, 'reluctant': 10}
{'happy': 40, 'tired': 20, 'angry': 5, 'alert': 70, 'reluctant': 5}
0
{'hold rope': 90, 'hold strings': 10, 'stand on one leg': 5, 'hold raft tightly': 5, 'focus on the target': 10}
{'hold rope': 90, 'hold strings': 10, 'stand on one leg': 5, 'hold raft tightly': 20, 'focus on the target': 5}
{'hold rope': 10, 'hold strings': 5, 'stand on one leg': 0, 'hold raft tightly': 90, 'focus on the target': 5}
3
{'walk forward': 20, 'jump down stage': 10, 'moving while singing': 30, 'touch their hands': 15, 'motioned with his head': 15}
{'walk forward': 40, 'jump down stage': 10, 'moving while singing': 70, 'touch their hands': 15, 'motioned with his head': 60}
{'walk forward': 20, 'jump down stage': 10, 'moving while singing': 30, 'touch their hands': 70, 'motioned with his head': 15}
2
{'hold the lady s hand': 10, 'drink from it': 5, 'walk over': 20, 'look at the man': 50, 'point to him and smile': 30}
{'hold the lady s hand': 10, 'drink from it': 5, 'walk over': 40, 'look at the man': 35, 'point to him and smile': 10}
{'hold the lady s hand': 5, 'drink from it': 5, 'walk over': 85, 'look at the man': 3, 'point to him and smile': 2}
2
{'five': 5, 'one': 25, 'four': 5, 'three': 5, 'two': 60}
{'five': 10, 'one': 50, 'four': 15, 'three': 20, 'two': 30}
{'five': 0, 'one': 90, 'four': 0, 'three': 0, 'two': 10}
4
{'wave to the girl': 10, 'sit down and drink water': 5, 'walks to the child': 30, 'talk': 35, 'pick up baby': 40}
{'wave to the girl': 5, 'sit down and drink water': 5, 'walks to the child': 5, 'talk': 80, 'pick up baby': 5}
{'wave to the girl': 5, 'sit down and drink water': 5, 'walks to the child': 5, 'talk': 80, 'pick up baby': 5}
3
{'carry him away': 10, 'hold his hand': 70, 'lift her up by pulling hands': 5, 'pulls it away': 60, 'open her arms': 5}
{'carry him away': 10, 'hold his hand': 40, 'lift her up by pulling hands': 5, 'pulls it away': 45, 'open her arms': 0}
{'carry him away': 10, 'hold his hand': 85, 'lift her up by pulling hands': 5, 'pulls it away': 10, 'open her arms': 10}
1
{'swipe off the person s hand': 5, 'lying on her belly': 10, 'sit up': 5, 'wearing a cap': 5, 'lying on her back': 75}
{'swipe off the person s hand': 5, 'lying on her belly': 90, 'sit up': 0, 'wearing a cap': 0, 'lying on her back': 5}
{'swipe off the person s hand': 5, 'lying on her belly': 5, 'sit up': 5, 'wearing a cap': 5, 'lying on her back': 80}
4
{'talk': 20, 'give her the toy back': 10, 'look away': 5, 'touch baby s head': 30, 'kiss baby': 25}
{'talk': 60, 'give her the toy back': 10, 'look away': 15, 'touch baby s head': 40, 'kiss baby': 30}
{'talk': 5, 'give her the toy back': 5, 'look away': 5, 'touch baby s head': 85, 'kiss baby': 0}
3
{'in his mouth': 5, 'with ball': 5, 'on the small table': 5, 'in his pocket': 5, 'on his waist': 10}
{'in his mouth': 5, 'with ball': 5, 'on the small table': 10, 'in his pocket': 60, 'on his waist': 20}
{'in his mouth': 5, 'with ball': 5, 'on the small table': 5, 'in his pocket': 10, 'on his waist': 75}
4
{'go to lady in stripes': 30, 'unwrap something': 10, 'adjust the girl s jacket': 25, 'shuffle cards': 5, 'play guitar': 5}
{'go to lady in stripes': 10, 'unwrap something': 20, 'adjust the girl s jacket': 15, 'shuffle cards': 5, 'play guitar': 5}
{'go to lady in stripes': 5, 'unwrap something': 50, 'adjust the girl s jacket': 10, 'shuffle cards': 20, 'play guitar': 5}
1
"""

# Split into blocks
lines = [l.strip() for l in raw.split('\n') if l.strip()]
examples = []
i = 0
while i + 3 < len(lines):
    d1 = ast.literal_eval(lines[i])
    d2 = ast.literal_eval(lines[i + 1])
    d3 = ast.literal_eval(lines[i + 2])
    answer_idx = int(lines[i + 3])
    keys = list(d1.keys())
    examples.append(((d1, d2, d3), keys, answer_idx))
    i += 4

def smart_vote(ds, margin=20):
    # ds: list of dicts, method 3 is ds[2]
    m3 = ds[2]
    sorted_vals = sorted(m3.values(), reverse=True)
    if len(sorted_vals) > 1 and (sorted_vals[0] - sorted_vals[1]) >= margin:
        # Method 3 is confident
        for k, v in m3.items():
            if v == sorted_vals[0]:
                return k
    # Else: Weighted sum (method 3 double weight)
    keys = list(ds[0].keys())
    scores = {k: ds[0][k] + ds[1][k] + 2 * ds[2][k] for k in keys}
    max_score = max(scores.values())
    tops = [k for k, v in scores.items() if v == max_score]
    if len(tops) == 1:
        return tops[0]
    # If still a tie, use majority-of-maximums among tied
    top_choices = []
    for d in ds:
        max_val = max(d.values())
        possible = [k for k, v in d.items() if v == max_val and k in tops]
        if possible:
            top_choices.append(possible[0])
        else:
            # If none of the tops present (shouldn't happen), just take one
            top_choices.append(list(tops)[0])
    from collections import Counter
    counts = Counter(top_choices)
    most_common = counts.most_common()
    max_count = most_common[0][1]
    best_candidates = [c for c, cnt in most_common if cnt == max_count]
    return best_candidates[0]



correct = 0
for ds, keys, gt_idx in examples:
    pred = smart_vote(ds)
    if pred == keys[gt_idx]:
        correct += 1

fraction_correct = correct / len(examples)

print(fraction_correct, correct, len(examples))
