import math
# Even + Even = Even
# Odd + Even = Odd
# Even + Odd = Odd
# Odd + Odd = Even


N = int(input())

lower = math.floor(N / 2)
higher = math.ceil(N / 2)

# Check to see if it can be perfectly split in half
if lower == higher:
    if lower % 2 == 1:
        print("Odd")
    else:
        print("Even")
else:
    print("Either")