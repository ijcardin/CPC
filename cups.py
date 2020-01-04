
cups = []

N = int(input())

for i in range(N):
    input1, input2 = input().split()

    # when diameter is given
    try:
        radius = int(input1) / 2
        cups.append((radius, input2))
    # when radius is given
    except ValueError:
        cups.append((int(input2), input1))


sortedByRadius = sorted(cups, key=lambda tup: tup[0])

for cup in sortedByRadius:
    print(cup[1])

