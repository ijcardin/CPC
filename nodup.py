userInput = input().split()
wordCollection = []
duplicate = False

for word in userInput:
    if word not in wordCollection:
        wordCollection.append(word)
    elif word in wordCollection:
        duplicate = True

if duplicate:
    print('no')
else:
    print('yes')

