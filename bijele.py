king, queen, rook, bishop, knight, pawn = map(int, input().split())
count = 0

while king != 1:
    if king < 1:
        king += 1
        count += 1
    elif king > 1:
        king -= 1
        count -= 1
print(count, end=' ')

count = 0
while queen != 1:
    if queen < 1:
        queen += 1
        count += 1
    elif queen > 1:
        queen -= 1
        count -= 1
print(count, end=' ')

count = 0
while rook != 2:
    if rook < 2:
        rook += 1
        count += 1
    elif rook > 2:
        rook -= 1
        count -= 1
print(count, end=' ')

count = 0
while bishop != 2:
    if bishop < 2:
        bishop += 1
        count += 1
    elif bishop > 2:
        bishop -= 1
        count -= 1
print(count, end=' ')

count = 0
while knight != 2:
    if knight < 2:
        knight += 1
        count += 1
    elif knight > 2:
        knight -= 1
        count -= 1
print(count, end=' ')

count = 0
while pawn != 8:
    if pawn < 8:
        pawn += 1
        count += 1
    elif pawn > 8:
        pawn -= 1
        count -= 1
print(count, end=' ')
