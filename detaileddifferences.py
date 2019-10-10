testCases = int(input())

for i in range(testCases):
    firstStr = input()
    secondStr = input()
    outputStr = ''
    
    print(firstStr)
    print(secondStr)
    for i in zip(firstStr, secondStr):
        if i[0] == i[1]:
            outputStr += '.'
        else:
            outputStr += '*'
    print(outputStr)
    print('')