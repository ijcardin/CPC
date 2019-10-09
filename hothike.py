# Hike is 3 days in total, hike to the lake for a full day, stay for a full day, hike back for a full day

lengthOfVacation = int(input())
dailyTemp = [int(n) for n in input().split()]
bestStartDay = 0
finalHighestTemp = 100  # initialize it to some value you know will be higher than anything the user inputs

for i in range(0, lengthOfVacation - 2):
    highestTemp = max(dailyTemp[i], dailyTemp[i + 2])
    if highestTemp < finalHighestTemp:
        finalHighestTemp = highestTemp
        bestStartDay = i + 1

print(bestStartDay, finalHighestTemp)


