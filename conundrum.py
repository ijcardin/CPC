cipherText = input()
dayCount = 0

for i in range(len(cipherText)):
    if i % 3 == 0 and cipherText[i] != 'P':
        dayCount += 1
    elif i % 3 == 1 and cipherText[i] != 'E':
        dayCount += 1
    elif i % 3 == 2 and cipherText[i] != 'R':
        dayCount += 1
    else:
        continue

print(dayCount)