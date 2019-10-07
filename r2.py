# S = (R1 + R2) / 2, R2 = (S*2) - R1

userInput = [int(n) for n in input().split()]
R1 = userInput[0]
S = userInput[1]

R2 = (S*2) - R1

print(R2)

