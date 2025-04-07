count = int(input())

numList = []

for _ in range(count):
  numList.append(list(map(int, input().split())))

for i in range(count - 2, -1, -1):
  for j in range(len(numList[i])):
    numList[i][j] = numList[i][j] + (numList[i + 1][j] if numList[i + 1][j] > numList[i + 1][j + 1] else numList[i + 1][j + 1])

print(numList[0][0])