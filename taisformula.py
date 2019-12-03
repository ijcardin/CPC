glucoseSamples = int(input())
tValues = []
vValues = []
area = 0

for i in range(glucoseSamples):
    t, v = map(float, input().split())
    tValues.append(t / 1000)
    vValues.append(v)

for i in range(len(tValues) - 1):
    area += ((vValues[i] + vValues[i + 1]) / 2) * (tValues[i + 1] - tValues[i])

print(area)
