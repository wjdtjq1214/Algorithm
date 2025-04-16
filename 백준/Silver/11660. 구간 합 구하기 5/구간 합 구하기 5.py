import sys

n, count = map(int, sys.stdin.readline().split())

sumList = []

for i in range(n):
  subSumList = []
  numList = list(map(int, sys.stdin.readline().split()))

  for j in range(n):
    if j == 0:
      subSumList.append(numList[j] + (sumList[i - 1][j] if i > 0 else 0))
    else:
      subSumList.append(subSumList[j - 1] + numList[j] + (sumList[i - 1][j] if i > 0 else 0) - (sumList[i - 1][j - 1] if i > 0 and j > 0 else 0))

  sumList.append(subSumList)

for _ in range(count):
  result = 0
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

  result += sumList[x2 - 1][y2 - 1] - (sumList[x2 - 1][y1 - 2] if x2 > 0 and y1 > 1 else 0) - (sumList[x1 - 2][y2 - 1] if x1 > 1 and y2 > 0 else 0) + (sumList[x1 - 2][y1 - 2] if x1 > 1 and y1 > 1 else 0)
  
  print(result)