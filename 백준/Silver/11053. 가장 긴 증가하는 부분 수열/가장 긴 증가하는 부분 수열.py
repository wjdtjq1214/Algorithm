length = int(input())
numList = list(map(int, input().split()))

maxCountList = [0 for _ in range(length)]

for i in range(length):
  maxCount = None

  for j in range(i):
    if numList[j] < numList[i] and (maxCount == None or maxCount < maxCountList[j]):
      maxCount = maxCountList[j]

  maxCountList[i] = 0 if maxCount == None else maxCount + 1

print(max(maxCountList) + 1)