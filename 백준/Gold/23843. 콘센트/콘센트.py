import math

deviceCount, outletCount = map(int, input().split())
deviceList = list(map(int, input().split()))

outletList = [0 for _ in range(outletCount)]
minValue = 0
result = 0

deviceList.sort()

while len(deviceList) > 0:
  result += minValue
  newMin = math.inf

  for i in range(len(outletList)):
    if outletList[i] == 0 or outletList[i] - minValue == 0:
      outletList[i] = deviceList.pop() if len(deviceList) > 0 else 0

      if newMin > outletList[i]:
        newMin = outletList[i]
    else:
      outletList[i] -= minValue

  minValue = newMin

print(result + max(outletList))