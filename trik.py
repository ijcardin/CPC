# 3 possible cups, labeled 1, 2, and 3. Ball initially in spot 1

borkoMoves = input()
initialSetup = ['1', '0', '0']
temp = 0

for letter in borkoMoves:
    if letter == 'A':
        initialSetup[0], initialSetup[1] = initialSetup[1], initialSetup[0]
    elif letter == 'B':
        initialSetup[1], initialSetup[2] = initialSetup[2], initialSetup[1]
    elif letter == 'C':
        initialSetup[0], initialSetup[2] = initialSetup[2], initialSetup[0]

print(initialSetup.index('1') + 1)
