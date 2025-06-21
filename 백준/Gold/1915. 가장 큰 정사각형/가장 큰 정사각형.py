import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sizeList = [[0 for _ in range(m)] for _ in range(n)]
max = 0

for i in range(n):
  inputStr = input().rstrip()

  for j in range(m):
    if inputStr[j] == '0' or i == 0 or j == 0:
      sizeList[i][j] = int(inputStr[j])
    else:
      sizeList[i][j] = min(sizeList[i - 1][j], sizeList[i][j - 1], sizeList[i - 1][j - 1]) + 1

    if sizeList[i][j] > max:
      max = sizeList[i][j]

print(max * max)