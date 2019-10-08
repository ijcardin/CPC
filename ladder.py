import math

userInput = [int(n) for n in input().split()]
h = userInput[0]
v = userInput[1]

ladderHeight = math.ceil(h / math.sin(math.radians(v)))
print(round(ladderHeight))