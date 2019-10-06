megabytesPerMonth = int(input())
numOfMonths = int(input())
dataUsed = []
savedMBs = megabytesPerMonth

for i in range(numOfMonths):
    dataUsed.append(int(input()))

for data in dataUsed:
    savedMBs = savedMBs - data
    savedMBs += megabytesPerMonth

print(savedMBs)
