from collections import defaultdict

myDict = defaultdict(lambda: -1)
myDict[1] = 1
myDict[2] = 1


def length(n):
    if n > 87:
        return -1
    if n not in myDict:
        myDict[n] = length(n-2) + length(n-1)
    return myDict[n]


def Fibonacci(n,k):
    if n == 1:
        return 'N'
    if n == 2:
        return 'A'
    l = length(n-2)
    while l == -1:
        n -= 1
        l = length(n - 2)
    if l < k:
        return Fibonacci(n - 1, k - l)
    return Fibonacci(n-2, k)

# list[0] is the Nth string
# list[1] is the Kth letter of the Nth string
myList = [int(n) for n in input().split()]
nthString = Fibonacci(myList[0], myList[1])

print(nthString)











