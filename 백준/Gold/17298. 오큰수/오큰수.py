numObjStack = []

listLen = int(input())

resultList = [str(-1) for _ in range(listLen)]

numList = input().split()
numObjList = [
  {
    "index": i,
    "num": int(numList[i])
  } for i in range(listLen)
]

i = 0

while i < listLen:
  numObj = numObjList[i]

  if len(numObjStack) == 0:
    numObjStack.append(numObj)
    i += 1
  else:
    lastStackObj = numObjStack.pop()

    if numObj["num"] > lastStackObj["num"]:
      resultList[lastStackObj["index"]] = str(numObj["num"])
    else:
      numObjStack.append(lastStackObj)
      numObjStack.append(numObj)
      i += 1

print(' '.join(resultList))