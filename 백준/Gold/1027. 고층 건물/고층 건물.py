count = int(input())
heightList = list(map(int, input().split()))

result = 0

for i in range(count):
  visibleCount = 0
  ratio = None

  for j in range(i - 1, -1, -1):
    newRatio = (heightList[j] - heightList[i]) / (i - j)

    if i - j == 1 or newRatio > ratio:
      ratio = newRatio
      visibleCount += 1

  ratio = None

  for j in range(i + 1, count):
    newRatio = (heightList[j] - heightList[i]) / (j - i)

    if j - i == 1 or newRatio > ratio:
      ratio = newRatio
      visibleCount += 1

  result = max(result, visibleCount)

print(result)