import math

costList = []
customerList = []

c, n = map(int, input().split())

for _ in range(n):
  cost, customer = map(int, input().split())

  costList.append(cost)
  customerList.append(customer)

sumCostList = [math.inf for _ in range(c + max(customerList) + 1)]
sumCostList[0] = 0

for i in range(1, c + max(customerList) + 1):
  for j in range(len(costList)):
    if i - customerList[j] >= 0 and sumCostList[i - customerList[j]] != math.inf and sumCostList[i - customerList[j]] + costList[j] < sumCostList[i]:
      sumCostList[i] = sumCostList[i - customerList[j]] + costList[j]

print(min(sumCostList[c:]))