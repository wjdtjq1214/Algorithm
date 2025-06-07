import sys

input = sys.stdin.readline

result = 0
heightList = []
indexList = []

count = int(input())

for i in range(count):
  height = int(input())

  while len(heightList) > 0 and heightList[-1] <= height:
    heightList.pop()
    lastIndex = indexList.pop()
    result += i - lastIndex - 1

  heightList.append(height)
  indexList.append(i)

for index in indexList:
  result += count - index - 1
  
print(result)