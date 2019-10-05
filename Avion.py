userInput = []
for i in range(5):
    userInput.append(input().upper())

caughtHim = False
for blimp in userInput:
    if 'FBI' in blimp:
        blimpNum = userInput.index(blimp) + 1
        caughtHim = True
        print(blimpNum, end=' ')

if caughtHim == False:
    print('HE GOT AWAY!')