import sys

input = sys.stdin.readline

inputString = input().rstrip()

while inputString != '0':
  stack = []
  max = 0

  heightList = (list(map(int, inputString.split())))[1:]

  for i in range(len(heightList)):
    height = heightList[i]
    lastIndex = i

    while len(stack) > 0 and stack[-1][1] > height:
      popList = stack.pop()
      size = popList[1] * (i - popList[0])
      lastIndex = popList[0]
      max = size if max < size else max

    if (len(stack) > 0 and stack[-1][1] != height) or len(stack) == 0:
      stack.append([lastIndex, height])

  for i in range(len(stack)):
    size = stack[i][1] * (len(heightList) - stack[i][0])
    max = size if max < size else max

  print(max)

  inputString = input().rstrip()