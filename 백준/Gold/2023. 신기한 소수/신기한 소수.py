import math

result = []
numList = ['2', '3', '5', '7']
appendNumList = ['1', '3', '7', '9']

length = int(input())

for _ in range(length - 1):
  newNumList = []

  for strNum in numList:
    for strAppendNum in appendNumList:
      newNumList.append(strNum + strAppendNum)

  for num in range(2, math.ceil(math.sqrt(int(newNumList[-1]))) + 1):
    for i in range(len(newNumList)):
      if newNumList[i] != '0' and int(newNumList[i]) % num == 0 and int(newNumList[i]) / num > 1:
        newNumList[i] = '0'

  numList = []

  for strNum in newNumList:
    if strNum != '0':
      numList.append(strNum)

for strNum in numList:
  print(strNum)