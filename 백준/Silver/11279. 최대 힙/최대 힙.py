import heapq
import sys

heap = []

numCount = int(sys.stdin.readline())

for _ in range(numCount):
  num = int(sys.stdin.readline()) * -1

  if num == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap) * -1)

    continue

  heapq.heappush(heap, num)