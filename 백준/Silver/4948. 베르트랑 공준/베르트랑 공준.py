import math

n = 123456

numList = [i for i in range((n * 2) + 1)]

for i in range(2, math.ceil(math.sqrt((n * 2) + 1))):
  for j in range(i + i, (n * 2) + 1, i):
    numList[j] = 0

numList[0] = 0
numList[1] = 0

num = int(input())

while num != 0:
  result = 0

  for i in range(num + 1, (num * 2) + 1):
    if numList[i] != 0:
      result += 1

  print(result)

  num = int(input())