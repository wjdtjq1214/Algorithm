import sys

input = sys.stdin.readline

result = 0
heightList = []
countList = []

count = int(input())

for i in range(count):
  inputHeight = int(input())

  flag = False
  lastHeight = inputHeight

  while len(heightList) > 0 and heightList[-1] < inputHeight:
    height = heightList.pop()
    lastCount = countList.pop()

    for j in range(lastCount + 1):
      result += j

    if len(countList) > 0:
      result += lastCount

  if len(heightList) > 0 and heightList[-1] == inputHeight:
    countList[-1] += 1
  else:
    heightList.append(inputHeight)
    countList.append(1)

while len(countList) > 0:
  lastCount = countList.pop()

  for j in range(lastCount):
    result += j

  if len(countList) > 0:
    result += lastCount
    
print(result)