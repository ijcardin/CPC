# First line of input contains integer L
# Second line contains integer D
# Third line contains integer X

L = int(input())
D = int(input())
X = int(input())

# Check minimal condition
for i in range(L, D + 1, 1):
    originalDigit = i
    sumOfDigits = 0
    while i:
        sumOfDigits += i % 10
        i //= 10
    if sumOfDigits == X:
        print(originalDigit)
        break

# Check maximal condition
for i in range(D, L - 1, -1):
    originalDigit = i
    sumOfDigits = 0
    while i:
        sumOfDigits += i % 10
        i //= 10
    if sumOfDigits == X:
        print(originalDigit)
        break



