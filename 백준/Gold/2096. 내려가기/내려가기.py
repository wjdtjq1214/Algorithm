import sys

input = sys.stdin.readline

maxResult = None
minResult = None

n = int(input())

minMaxList = [[0, 0] for _ in range(3)]

for i in range(n):
  newMinMaxList = [[] for _ in range(3)]

  numList = list(map(int, input().split()))

  for j in range(3):
    minValue = None
    maxValue = None
    
    for k in range(j - 1 if j != 0 else j, (j + 1 if j != 2 else j) + 1):
      minValue = minMaxList[k][0] if minValue == None or minValue > minMaxList[k][0] else minValue
      maxValue = minMaxList[k][1] if maxValue == None or maxValue < minMaxList[k][1] else maxValue

    minValue += numList[j]
    maxValue += numList[j]

    if i == n - 1:
      minResult = minValue if minResult == None or minResult > minValue else minResult
      maxResult = maxValue if maxResult == None or maxResult < maxValue else maxResult

    newMinMaxList[j].append(minValue)
    newMinMaxList[j].append(maxValue)

  minMaxList = newMinMaxList

print(maxResult, minResult)