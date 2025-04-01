indexList = []
indexDic = {}

input()

numList = list(map(int, input().split()))

setList = list(set(numList))
setList.sort()

for i in range(0, len(setList)):
  indexDic[setList[i]] = i

for num in numList:
  indexList.append(str(indexDic[num]))

print(' '.join(indexList))