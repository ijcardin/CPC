
limit, numOfGroups = map(int, input().split())
currentNum = 0
rejectedGroups = 0

for x in range(numOfGroups):
    status, num = input().split()

    if status == "enter":
        if currentNum + int(num) <= limit:
            currentNum += int(num)
        else:
            rejectedGroups += 1
    elif status == "leave":
        currentNum -= int(num)

print(rejectedGroups)
