periods = int(input())
QALY = 0

for i in range(periods):
    q, y = input().split()
    QALY += float(q)*float(y)

print(round(QALY, 3))