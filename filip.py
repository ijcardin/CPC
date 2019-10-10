num1, num2 = input().split()

backwardsNum1 = ''
backwardsNum2 = ''

for i in range(2,-1, -1):
    backwardsNum1 += num1[i]
    backwardsNum2 += num2[i]

print(max(int(backwardsNum1), int(backwardsNum2)))



