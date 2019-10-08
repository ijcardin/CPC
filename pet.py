highestScore = 0
highestRank = 1
playerScore = []

for i in range(1, 6):
    playerScore = [int(n) for n in input().split()]
    totalScore = 0
    for score in playerScore:
        totalScore += score
    if totalScore > highestScore:
        highestScore = totalScore
        highestRank = i

print(highestRank, highestScore)