import sys
import heapq

input = sys.stdin.readline

testCount = int(input())

for _ in range(testCount):
  numList = []
  printList = []
  firstHeap = []
  secondHeap = []

  numCount = int(input())

  for _ in range(numCount // 10 + 1):
    numList += list(map(int, input().rstrip().split()))

  for i in range(numCount):
    if len(firstHeap) == len(secondHeap):
      if len(firstHeap) == 0 or numList[i] <= secondHeap[0]:
        heapq.heappush(firstHeap, -numList[i])
      else:
        heapq.heappush(secondHeap, numList[i])
        heapq.heappush(firstHeap, -heapq.heappop(secondHeap))
    else:
      if numList[i] >= -firstHeap[0]:
        heapq.heappush(secondHeap, numList[i])
      else:
        heapq.heappush(firstHeap, -numList[i])
        heapq.heappush(secondHeap, -heapq.heappop(firstHeap))

    if i % 2 == 0:
      printList.append(-firstHeap[0])

  print(len(printList))
  print(' '.join(list(map(str, printList))))