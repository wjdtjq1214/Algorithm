import sys

input = sys.stdin.readline

setIdList = []
setDic = {}

n, m = map(int, input().rstrip().split())

for i in range(n + 1):
  setIdList.append(i)
  setDic[i] = [i]

for _ in range(m):
  a, b = map(int, input().rstrip().split())

  if a == b or setIdList[a] == setIdList[b]:
    continue

  setId = setIdList[a] if setIdList[a] < setIdList[b] else setIdList[b]
  changeSetId = setIdList[a] if setIdList[a] > setIdList[b] else setIdList[b]

  for i in setDic[changeSetId]:
    setIdList[i] = setId
    setDic[setId].append(i)
  
  del setDic[changeSetId]

print(len(setDic) - 1)