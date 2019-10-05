numberOfIntegers = int(input())
numbers = []

for i in range(numberOfIntegers):
    num = int(input())
    if num:
        numbers.append(num)
sum = 0
for num in numbers:
    base = num // 10
    exp = num % 10
    finalNum = base**exp
    sum += finalNum
print(sum)
