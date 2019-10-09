inputWord = input()
sCount = 0
hiss = False

for i in range(len(inputWord)):
    if inputWord[i] == 's':
        sCount += 1
        if sCount >= 2:
            hiss = True
            break
    else:
        sCount = 0

if hiss:
    print('hiss')
else:
    print('no hiss')
