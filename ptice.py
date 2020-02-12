
adrianSequence = "ABC" * 34
brunoSequence = "BABC" * 25
goranSequence = "CCAABB" * 17

N = int(input())
answers = input()

adrianScore = 0
brunoScore = 0
goranScore = 0

adrianSequence = adrianSequence[0:N]
brunoSequence = brunoSequence[0:N]
goranSequence = goranSequence[0:N]

for i in range(N):
    if answers[i] == adrianSequence[i]:
        adrianScore += 1
    if answers[i] == brunoSequence[i]:
        brunoScore += 1
    if answers[i] == goranSequence[i]:
        goranScore += 1

answerTracker = {"Adrian": adrianScore, "Bruno": brunoScore, "Goran": goranScore}
finalAnswer = {}

for key, value in sorted(answerTracker.items()):
    finalAnswer.setdefault(value, []).append(key)

print(sorted(finalAnswer, reverse=True)[0])

for name in sorted(finalAnswer[sorted(finalAnswer, reverse=True)[0]]):
    print(name)

