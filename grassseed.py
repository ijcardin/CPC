C = float(input())
L = int(input())
totalCost = 0

for i in range(L):
    userInput = [float(n) for n in input().split()]
    w = userInput[0]
    l = userInput[1]

    totalCost += C*w*l

print(round(totalCost, 6))
