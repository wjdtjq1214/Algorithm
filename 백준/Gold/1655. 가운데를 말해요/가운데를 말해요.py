import sys
import heapq

input = sys.stdin.readline

heap1 = []
heap2 = []

count = int(input())

for _ in range(count):
  num = int(input())

  if len(heap1) == len(heap2):
    if len(heap1) == 0 or num <= heap2[0]:
      heapq.heappush(heap1, -num)
    else:
      heapq.heappush(heap1, -heapq.heappop(heap2))
      heapq.heappush(heap2, num)
  else:
    if num <= -heap1[0]:
      heapq.heappush(heap2, -heapq.heappop(heap1))
      heapq.heappush(heap1, -num)
    else:
      heapq.heappush(heap2, num)
  
  print(-heap1[0])