n, k = map(int, input().split())

countList = [1] * (n + 1)

for _ in range(1, k):
  newCountList = [0] * (n + 1)

  for i in range(0, n + 1):
    for j in range(0, n - i + 1):
      newCountList[i + j] += countList[i]

  countList = newCountList

print(countList[-1] % 1000000000)