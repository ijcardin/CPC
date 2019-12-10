
testCases = int(input())

for x in range(testCases):
    command = input()
    if command.startswith("Simon says "):
        print(command.replace("Simon says ", ''))
