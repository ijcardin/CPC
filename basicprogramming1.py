import statistics

myDict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
          13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y',
          25: 'z'}

N, t = map(int, input().split())

A = [int(x) for x in input().split()]

if t == 1:
    print(7)
elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    print(statistics.median([A[0], A[1], A[2]]))
elif t == 4:
    mySum = 0
    for i in range(len(A)):
        mySum += A[i]
    print(mySum)
elif t == 5:
    mySum = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            mySum += A[i]
    print(mySum)
elif t == 6:
    outputStr = ''

    for num in A:
        outputStr += myDict[num % 26]

    print(outputStr)

elif t == 7:
    currentIndex = A[A[0]]
    visited = []
    visited.append(currentIndex)

    while currentIndex <= len(A) - 1:
        if currentIndex > len(A) - 1:
            print("out")
        elif currentIndex == len(A) - 1:
            print("done")
        else:
            if currentIndex in visited:
                print("Cyclic")
                break
            currentIndex = A[A[currentIndex]]
            visited.append(currentIndex)


