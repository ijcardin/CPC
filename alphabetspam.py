testStr = input()

whitespaceCount = 0
lowercaseCount = 0
uppercaseCount = 0
symbolCount = 0

for letter in testStr:
    if letter == '_':
        whitespaceCount += 1
    elif letter.islower():
        lowercaseCount += 1
    elif letter.isupper():
        uppercaseCount += 1
    else:
        symbolCount += 1

print(whitespaceCount / len(testStr))
print(lowercaseCount / len(testStr))
print(uppercaseCount / len(testStr))
print(symbolCount / len(testStr))