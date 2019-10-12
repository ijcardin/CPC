name = input()
newName = ''

for i in range(len(name) - 1):
    if name[i] == name[i + 1]:
        continue
    else:
        newName += name[i]
newName += name[-1]

print(newName)
