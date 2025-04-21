resultSet = set()

n, m = map(int, input().split())
numList = [i for i in range(1, n + 1)]

def createNum(createdNumList, leftNumList):
  if len(createdNumList) == m and ' '.join(createdNumList) not in resultSet:
    resultSet.add(' '.join(createdNumList))
    print(' '.join(createdNumList))
  else:
    for i in range(len(leftNumList)):
      createNum(createdNumList + [str(leftNumList[i])], leftNumList[0:i] + leftNumList[i + 1:])

createNum([], numList)