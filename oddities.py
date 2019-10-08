numberOfTestCases = int(input())
testCases = []

for i in range(numberOfTestCases):
    testCases.append(int(input()))

for testCase in testCases:
    if testCase % 2 == 0:
        print(testCase, 'is even')
    else:
        print(testCase, 'is odd')