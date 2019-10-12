n = int(input())
stats = list(map(float, input().split()))
sum = 0
slugCount = 0

for stat in stats:
    if stat != -1:
        sum += stat
        slugCount += 1

print(sum/slugCount)