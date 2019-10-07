import math

userInput = [int(n) for n in input().split()]
N = userInput[0]
W = userInput[1]
H = userInput[2]
matchLengths = []

for i in range(N):
    matchLengths.append(int(input()))

for length in matchLengths:
    if length > math.sqrt(W**2 + H**2):
        print('NE')
    else:
        print('DA')


