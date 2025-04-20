num = int(input())

countList = [[0, 0] for _ in range(num + 1)]

for i in range(2, num + 1):
  minCount = None
  prevIndex = None

  if i % 2 == 0:
    minCount = countList[i // 2][0] + 1
    prevIndex = i // 2

  if i % 3 == 0 and (minCount == None or (countList[i // 3][0] + 1 < minCount)):
    minCount = countList[i // 3][0] + 1
    prevIndex = i // 3

  if minCount == None or (countList[i - 1][0] + 1 < minCount):
    minCount = countList[i - 1][0] + 1
    prevIndex = i - 1

  countList[i] = [minCount, prevIndex]

index = num
indexList = [str(index)]

while index != 1:
  index = countList[index][1]
  indexList.append(str(index))

print(countList[-1][0])
print(' '.join(indexList))