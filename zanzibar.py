
testCases = int(input())

for x in range(testCases):

    turtleInput = [x for x in input().split()]
    cursor = 0
    importedTurtles = 0

    while cursor < len(turtleInput):
        try:
            if int(turtleInput[cursor + 1]) > int(turtleInput[cursor]) * 2:
                importedTurtles += int(turtleInput[cursor + 1]) - (int(turtleInput[cursor]) * 2)
        except:
            pass
        cursor += 1

    print(importedTurtles)