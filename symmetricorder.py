
n = 1
while True:
    numOfNames = input()
    if numOfNames == '0':
        break
    listOfNames = []

    for x in range(int(numOfNames)):
        listOfNames.append(input())

    left = 1
    right = len(listOfNames) - 1

    while left <= right:
        poppedName = listOfNames.pop(left)
        listOfNames.insert(right, poppedName)
        left += 1
        right -= 1

    print("SET " + str(n))

    for name in listOfNames:
        print(name)
    n += 1


