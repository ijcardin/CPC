userInput = [int(n) for n in input().split()]
X = userInput[0]
Y = userInput[1]
N = userInput[2]

for i in range(1, N + 1):
    if i % X == 0 and i % Y == 0:
        print('FizzBuzz')
    elif i % X == 0:
        print('Fizz')
    elif i % Y == 0:
        print('Buzz')
    else:
        print(i)