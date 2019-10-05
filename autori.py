seperateWords = [word for word in input().split('-')]
abbrev = ''

for word in seperateWords:
    abbrev += word[0]

print(abbrev)
