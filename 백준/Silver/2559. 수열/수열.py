sum = 0

tampCount, sumCount = map(int, input().split())
tampList = list(map(int, input().split()))

for i in range(sumCount):
  sum += tampList[i]

sumMax = sum

for i in range(tampCount - sumCount):
  sum -= tampList[i]
  sum += tampList[i + sumCount]

  if sum > sumMax:
    sumMax = sum

print(sumMax)