targetNum = int(input())
countList = [-1 for i in range(targetNum + 1)]

countList[0] = 0
countList[1] = 0

for i in range(2, targetNum + 1):
  countNumList = []

  if i % 3 == 0:
    countNumList.append(countList[i // 3] + 1)

  if i % 2 == 0:
    countNumList.append(countList[i // 2] + 1)

  countNumList.append(countList[i - 1] + 1)

  countList[i] = min(countNumList)

print(countList[targetNum])