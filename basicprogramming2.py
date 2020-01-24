import statistics

N, t = map(int, input().split())
myDict = {}

A = [int(x) for x in input().split()]

if t == 1:

    doesExist = False
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] != A[j] and A[i] + A[j] == 7777:
                doesExist = True
                break
    if doesExist:
        print('Yes')
    else:
        print("No")

elif t == 2:
    if len(A) == len(set(A)):
        print("Unique")
    else:
        print("Contains duplicate")

elif t == 3:
    for integer in A:
        myDict[integer] = myDict.get(integer, 0) + 1

    for key, value in myDict.items():
        if value > N/2:
            print(key)
            break
        else:
            print(-1)

elif t == 4:
    if N % 2 != 0:
        print(statistics.median(A))
    else:
        A.sort()
        print(A[int(len(A)/2) - 1], A[int(len(A)/2)])

elif t == 5:
    A.sort()

    for num in A:
        if num >= 100 and num <= 999:
            print(num, end=' ')
