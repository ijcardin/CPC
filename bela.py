N, B = input().split()
points = 0

dominantSuit = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
nonDominantSuit = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

for i in range(4*int(N)):
    card = input()
    if card[1] == B:
        points += dominantSuit[card[0]]
    else:
        points += nonDominantSuit[card[0]]

print(points)
