
l, r = map(int, input().split())

if l == r and l != 0 and r != 0:
    print('Even ' + str(l + r))
elif l > r:
    print('Odd ' + str(l * 2))
elif r > l:
    print('Odd ' + str(r * 2))
else:
    print("Not a moose")