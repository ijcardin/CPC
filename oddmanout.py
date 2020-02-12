
testCases = int(input())
case = 1

for x in range(testCases):
    guestCodes = {}
    G = int(input())
    guests = [int(x) for x in input().split()]

    for guest in guests:
        guestCodes[guest] = guestCodes.get(guest, 0) + 1

    for guestCode, count in guestCodes.items():
        if count == 1:
            print("Case #" + str(case) + ": " + str(guestCode))

    case += 1


