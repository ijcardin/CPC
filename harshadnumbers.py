
n = int(input())

while True:
    sum = 0
    num = n

    while num:
        digit = num % 10
        sum += digit
        num //= 10

    if n % sum == 0:
        break
    else:
        n += 1

print(n)


