
while True:
    n = int(input())
    totalMiles = 0
    oldTime = 0
    currentTime = 0
    if n == -1:
        break
    for i in range(n):
        speed, time = map(int, input().split())
        currentTime = time - oldTime
        totalMiles += speed * currentTime
        oldTime = time
    print(totalMiles, 'miles')