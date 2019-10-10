N, M = map(int,input().split())

if N == M:
    print(N + 1)
else:
    numberOfAnswers = abs(N-M)+1
    start = min(N, M) + 1
    for i in range(start, start + numberOfAnswers):
        print(i)

