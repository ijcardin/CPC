
while True:
    numerator, denominator = map(int, input().split())
    if numerator == 0 and denominator == 0:
        break

    wholeNum = numerator // denominator
    remainder = numerator % denominator

    print(str(wholeNum) + ' ' + str(remainder) + ' / ' + str(denominator))

