length = int(input())
budgetArr = list(map(int, input().split()))
budget = int(input())

average = budget // length

while min(budgetArr) <= average and max(budgetArr) > average:
  newBudgetArr = []

  for num in budgetArr:
    if num <= average:
      budget -= num
    else:
      newBudgetArr.append(num)


  budgetArr = newBudgetArr
  average = budget // len(budgetArr)

if min(budgetArr) > average:
  print(budget // len(budgetArr))
else:
  print(max(budgetArr))