numStack = []

numCount = int(input())
numList = list(map(int, input().split()))

result = [str(-1) for _ in range(numCount)]

for index in range(numCount):
  num = numList[index]

  while len(numStack) > 0 and numStack[-1]['num'] < num:
    result[numStack.pop()['index']] = str(num)

  numStack.append({
    'index': index,
    'num': num
  })

print(' '.join(result))