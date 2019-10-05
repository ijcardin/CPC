numberOfTemperatures = int(input())
listOfTemps = [int(n) for n in input().split()]
count = 0

for temp in listOfTemps:
    if temp < 0:
        count += 1

print(count)