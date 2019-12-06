
cards = input()

TCounter = 0
GCounter = 0
CCounter = 0
score = 0

for card in cards:

    if card == 'T':
        TCounter += 1
    elif card == 'G':
        GCounter += 1
    elif card == 'C':
        CCounter += 1

    score = TCounter**2 + GCounter**2 + CCounter**2

while TCounter >= 1 and GCounter >= 1 and CCounter >= 1:
    score += 7
    TCounter -= 1
    GCounter -= 1
    CCounter -= 1

print(score)

