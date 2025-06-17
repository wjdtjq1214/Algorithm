count = int(input())
fixedCount = int(input())

listLenList = []
lastFixed = None
result = 1

for i in range(fixedCount):
  fixed = int(input().strip())

  if i == 0:
    listLenList.append(fixed - 1)
  else:
    listLenList.append(fixed - lastFixed - 1)
  
  lastFixed = fixed

if fixedCount == 0:
  listLenList.append(count)
else:
  listLenList.append(count - sum(listLenList) - fixedCount)

countList = [0 for _ in range(count + 1)]
countList[0] = 1
countList[1] = 1

for i in range(2, count + 1):
  countList[i] = countList[i - 1] + countList[i - 2]

for listLen in listLenList:
  result *= countList[listLen]
  
print(result)