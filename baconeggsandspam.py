
foodList = {}

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        userOrder = [x for x in input().split()]
        name = userOrder[0]

        userOrder.pop(0)

        for food in userOrder:
            if food not in foodList:
                foodList[food] = []
            foodList[food].append(name)

    for key in sorted(foodList):
        names = ''
        for name in sorted(foodList[key]):
            names += name + ' '

        print(key + ' ' + names)

    print()
    foodList = {}




