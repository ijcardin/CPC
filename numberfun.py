testCases = int(input())

for i in range(testCases):
    num1, num2, result = map(int, input().split())

    # addition
    if num1 + num2 == result:
        print("Possible")
    # subtraction
    elif num1 - num2 == result:
        print("Possible")
    elif num2 - num1 == result:
        print("Possible")
    # multiplication
    elif num1 * num2 == result:
        print("Possible")
    # division
    elif num1 / num2 == result:
        print("Possible")
    elif num2 / num1 == result:
        print("Possible")
    else:
        print("Impossible")
