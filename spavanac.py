inputTime = [int(n) for n in input().split()]
hour = inputTime[0]
minute = inputTime[1]

newMinute = (minute - 45) % 60

if minute - 45 < 0:
    newHour = (hour - 1) % 24
    print(newHour, newMinute)
else:
    print(hour, newMinute)

