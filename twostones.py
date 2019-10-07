# odd number of stones, alice wins
# else, bob wins

numOfStones = int(input())

while True:
    if numOfStones == 0:
        print('Bob')
        break
    elif numOfStones == 1:
        print('Alice')
        break
    numOfStones -= 2
