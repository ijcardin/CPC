import math
n, h, v = map(int, input().split())

middle = math.ceil(n / 2)

if h < middle:
    h = n - h
if v < middle:
    v = n - v

print(4*h*v)
