lengthStack = []

listLen = int(input())

resultList = [0 for _ in range(listLen)]

lengthList = list(map(int, input().split()))
lengthNodeList = [
  {
    "index": i + 1,
    "length": lengthList[i]
  } for i in range(listLen)
]

while len(lengthStack) > 0 or len(lengthNodeList) > 0:
  if len(lengthStack) == 0:
    lengthStack.append(lengthNodeList.pop())
  else:
    stackNode = lengthStack.pop()

    if len(lengthNodeList) == 0:
      resultList[stackNode["index"] - 1] = '0'
    else:
      listNode = lengthNodeList.pop()

      if stackNode["length"] <= listNode["length"]:
        resultList[stackNode["index"] - 1] = str(listNode["index"])

        lengthNodeList.append(listNode)
      else:
        lengthStack.append(stackNode)
        lengthStack.append(listNode)

print(' '.join(resultList))