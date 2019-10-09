testCases = int(input())

for i in range(testCases):
    userInput = [float(n) for n in input().split()]
    b = userInput[0]
    p = userInput[1]
    BPM = (60 * b) / p
    ABPM = 60 / p

    print(round(BPM - ABPM, 4), round(BPM, 4), round(BPM + ABPM, 4))