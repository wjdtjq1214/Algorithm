import sys
import heapq
input = sys.stdin.readline

result = 0
speechList = []
speechHeap = []

n = int(input().rstrip())

for _ in range(n):
  p, d = map(int, input().rstrip().split())

  speechList.append((p, d))

speechList.sort(key=lambda x: (-x[1], x[0]))

while len(speechList) > 0:
  if len(speechHeap) < speechList[-1][1]:
    result += speechList[-1][0]
    heapq.heappush(speechHeap, speechList[-1][0])
  elif speechHeap[0] < speechList[-1][0]:
    result += speechList[-1][0] - heapq.heappop(speechHeap)
    heapq.heappush(speechHeap, speechList[-1][0])

  speechList.pop()

print(result)