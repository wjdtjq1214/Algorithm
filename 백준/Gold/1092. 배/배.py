import math

craneCount = int(input())
craneList = list(map(int, input().split()))
boxCount = int(input())
boxList = list(map(int, input().split()))

flag = False
maxCraneWeight = max(craneList)
craneBoxList = [0 for _ in range(craneCount)]

craneList.sort()

for boxWeight in boxList:
  if boxWeight > maxCraneWeight:
    flag = True
    break

  for i in range(craneCount):
    if craneList[i] >= boxWeight:
      craneBoxList[i] += 1
      break

if flag:
  print(-1)
else:
  for i in range(craneCount - 1):
    craneBoxCount = craneBoxList[i]
    boxCountAvg = math.ceil(boxCount / (craneCount - i))

    if boxCountAvg < craneBoxCount:
      craneBoxList[i + 1] += craneBoxList[i] - boxCountAvg
      craneBoxList[i] = boxCountAvg
      boxCount -= boxCountAvg
    else:
      boxCount -= craneBoxCount

  print(max(craneBoxList))