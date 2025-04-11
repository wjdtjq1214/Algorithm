numObj = {}
numStack = []

numCount = int(input())
numList = list(map(int, input().split()))

result = [str(-1) for _ in range(numCount)]

for num in numList:
  if num in numObj:
    numObj[num] += 1
  else:
    numObj[num] = 1

for index in range(numCount):
  num = numList[index]

  while len(numStack) > 0 and numObj[numStack[-1]['num']] < numObj[num]:
    result[numStack.pop()['index']] = str(num)

  numStack.append({
    'index': index,
    'num': num
  })

print(' '.join(result))