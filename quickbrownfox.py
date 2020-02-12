import collections

testCases = int(input())

for x in range(testCases):
    letterTracker = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                     'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                     'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                     'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    str = input()
    missingLetters = ''
    cleanStr = ''.join(c.lower() for c in str if c.isalpha())

    for char in cleanStr:
        letterTracker[char] = letterTracker.get(char, 0) + 1

    orderedDict = collections.OrderedDict(sorted(letterTracker.items()))

    for key, value in orderedDict.items():
        if value == 0:
            missingLetters += key

    if missingLetters == '':
        print('pangram')
    else:
        print('missing ' + missingLetters)




