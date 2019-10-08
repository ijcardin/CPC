n = int(input())
output = []

for i in range(n):
    userInput = [int(x) for x in input().split()]
    r = userInput[0]
    e = userInput[1]
    c = userInput[2]

    if e - c > r:
        output.append('advertise')
    elif e - c < r:
        output.append('do not advertise')
    else:
        output.append('does not matter')

for output in output:
    print(output)