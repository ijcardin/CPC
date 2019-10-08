testCases = int(input())
uniqueCities = []

for i in range(testCases):
    numberOfCities = int(input())
    cities = []
    for i in range(numberOfCities):
        city = input()
        if city not in cities:
            cities.append(city)
    uniqueCities.append(len(cities))

for num in uniqueCities:
    print(num)