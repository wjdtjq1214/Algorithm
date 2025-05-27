numCount = int(input())
numList = list(map(int, input().split()))

calNumObj = {
  numList[0]: 1
}

for num in numList[1: -1]:
  newCalNumObj = {}

  for calNumStr in calNumObj:
    calNum = int(calNumStr)
    
    if 0 <= calNum + num <= 20:
      if calNum + num not in newCalNumObj:
        newCalNumObj[calNum + num] = calNumObj[calNumStr]
      else:
        newCalNumObj[calNum + num] += calNumObj[calNumStr]

    if 0 <= calNum - num <= 20:
      if calNum - num not in newCalNumObj:
        newCalNumObj[calNum - num] = calNumObj[calNumStr]
      else:
        newCalNumObj[calNum - num] += calNumObj[calNumStr]

  calNumObj = newCalNumObj

if numList[-1] not in calNumObj:
  print(0)
else:
  print(calNumObj[numList[-1]])