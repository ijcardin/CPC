dataSets = int(input())

for x in range(dataSets):
    K, b, n = map(int, input().split())
    sum = 0
    digit = 0
    while n > 0:
        digit = n % b
        sum += digit * digit
        n = (n - digit) / b

    print(K, int(sum))
