N = int(input())
beverage = input()

for i in range(N, 0, -1):
    if i - 1 == 0:
        print(str(i) + " bottle of " + beverage + " on the wall, " + str(i) + " bottle of " + beverage + ".")
        print("Take it down, pass it around, no more bottles of " + beverage + ".")
    elif i - 1 == 1:
        print(str(i) + " bottles of " + beverage + " on the wall, " + str(i) + " bottles of " + beverage + ".")
        print("Take one down, pass it around, " + str(i - 1) + " bottle of " + beverage + " on the wall.")
    else:
        print(str(i) + " bottles of " + beverage + " on the wall, " + str(i) + " bottles of " + beverage + ".")
        print("Take one down, pass it around, " + str(i - 1) + " bottles of " + beverage + " on the wall.")
    print()