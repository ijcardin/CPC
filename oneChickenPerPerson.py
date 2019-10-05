userInput = [int(line) for line in input().split()]

numberOfPeople = userInput[0]
numberOfChicken = userInput[1]

if numberOfPeople > numberOfChicken:
    diff = numberOfPeople - numberOfChicken
    if diff == 1:
        print("Dr. Chaz needs 1 more piece of chicken!")
    else:
        print('Dr. Chaz needs ' + str(diff) + ' more pieces of chicken!')
else:
    diff = numberOfChicken - numberOfPeople
    if diff == 1:
        print("Dr. Chaz will have 1 piece of chicken left over!")
    else:
        print('Dr. Chaz will have ' + str(diff) + ' pieces of chicken left over!')









