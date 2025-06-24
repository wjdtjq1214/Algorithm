import sys
import heapq

input = sys.stdin.readline

count = int(input())

startEndTimeList = []
roomHeap = []

for _ in range(count):
  startEndTimeList.append(list(map(int, (input().split())[1:])))

startEndTimeList.sort(key=lambda x: (x[0], x[1]))

for [start, end] in startEndTimeList:
  if len(roomHeap) == 0 or roomHeap[0] > start:
    heapq.heappush(roomHeap, end)
  else:
    heapq.heappop(roomHeap)
    heapq.heappush(roomHeap, end)

print(len(roomHeap))