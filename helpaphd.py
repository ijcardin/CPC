N = int(input())

for i in range(N):
    userInput = input()
    if userInput[0] == 'P':
        print('skipped')
    else:
        nums = [int(s) for s in userInput.split('+') if s.isdigit()]
        print(nums[0] + nums[1])