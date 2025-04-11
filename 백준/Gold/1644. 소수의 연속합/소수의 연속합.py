import math
from collections import deque

result = 0
sum = 0
numList = []
numQueue = deque()

inputNum = int(input())

tempList = [i for i in range(inputNum + 1)]

for i in range(2, math.ceil(math.sqrt(inputNum)) + 1):
  for j in range(i + i, inputNum + 1, i):
    tempList[j] = 0

tempList[1] = 0

for num in tempList:
  if num != 0:
    numList.append(num)

for num in numList:
  sum += num
  numQueue.append(num)

  if len(numQueue) == 1 and sum > inputNum:
    break

  while sum > inputNum:
    sum -= numQueue.popleft()

  if sum == inputNum:
    result += 1

print(result)