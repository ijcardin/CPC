numberOfExpenses = input()
sumOfExpenses = sum(-x for x in map(int, input().split()) if x < 0)
print(sumOfExpenses)








