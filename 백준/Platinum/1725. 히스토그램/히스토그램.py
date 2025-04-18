import sys

input = sys.stdin.readline
stack = []
max = 0

count = int(input())

for i in range(count):
  height = int(input())
  lastIndex = i

  while len(stack) > 0 and stack[-1][1] > height:
    popList = stack.pop()
    size = popList[1] * (i - popList[0])
    lastIndex = popList[0]
    max = size if max < size else max

  if (len(stack) > 0 and stack[-1][1] != height) or len(stack) == 0:
    stack.append([lastIndex, height])

for i in range(len(stack)):
  size = stack[i][1] * (count - stack[i][0])
  max = size if max < size else max

print(max)