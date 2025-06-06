import sys
import heapq

input = sys.stdin.readline

numHeap = []
result = 0

count = int(input())

for _ in range(count):
  heapq.heappush(numHeap, int(input().rstrip()))

while len(numHeap) > 1:
  first = heapq.heappop(numHeap)
  second = heapq.heappop(numHeap)

  heapq.heappush(numHeap, first + second)

  result += first + second

print(result)