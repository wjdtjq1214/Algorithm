import math

count, total = map(int, input().split())

countList = [math.inf] * (total + 1)
countList[0] = 0
coinList = []

for _ in range(count):
  coinList.append(int(input()))

for i in range(1, total + 1):
  for coin in coinList:
    if i - coin >= 0 and countList[i - coin] != math.inf and countList[i] > countList[i - coin] + 1:
      countList[i] = countList[i - coin] + 1

print(countList[total] if countList[total] != math.inf else -1)