import sys
import math

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
  numArr = []

  n = int(input().rstrip())

  sumList = [[-math.inf for _ in range(n)] for _ in range(2)]
  
  numArr.append(list(map(int, input().rstrip().split())))
  numArr.append(list(map(int, input().rstrip().split())))

  for i in range(0, n):
    for j in range(0, 2):
      if j == 0:
        if i == 0:
          sumList[j][i] = numArr[j][i]
        else:
          sumList[j][i] = max(numArr[j][i] + sumList[1][i - 1], sumList[0][i - 1])
      else:
        if i == 0:
          sumList[j][i] = numArr[j][i]
        else:
          sumList[j][i] = max(numArr[j][i] + sumList[0][i - 1], sumList[1][i - 1])
          
  print (max(sumList[0][n - 1], sumList[1][n - 1]))