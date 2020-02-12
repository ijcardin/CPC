distinctNum = []


for i in range(10):
    num = int(input()) % 42

    if num not in distinctNum:
        distinctNum.append(num)

print(len(distinctNum))
