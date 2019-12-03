
def sumDigit(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

while True:
    testCase = int(input())
    if testCase == 0:
        break
    sumOfDigits = sumDigit(testCase)
    for i in range(100000):
        if i > 10 and sumDigit(i * testCase) == sumOfDigits:
            print(i)
            break
