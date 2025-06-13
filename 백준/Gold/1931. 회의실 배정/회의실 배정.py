import sys

input = sys.stdin.readline

timeList = []
endTime = 0
result = 0

count = int(input())

for _ in range(count):
  start, end = map(int, input().split())
  
  timeList.append([start, end])

timeList.sort(key=lambda x: (x[0], x[1]))

for [start, end] in timeList:
  if start >= endTime:
    result += 1
    endTime = end
  elif end < endTime:
    endTime = end

print(result)