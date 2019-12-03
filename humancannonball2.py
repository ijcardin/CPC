import math

testCases = int(input())
for i in range(testCases):
    v, theta, x, h1, h2 = map(float, input().split())
    time = (x / v) / math.cos(math.radians(theta))
    y = (v * time * math.sin(math.radians(theta))) - 0.5 * 9.81 * time**2

    if y > h1 + 1 and y < h2 - 1:
        print('Safe')
    else:
        print('Not Safe')

