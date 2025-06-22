import sys
import heapq
import math

input = sys.stdin.readline

maxCount = 0
maxCountNumArray = []
max = -math.inf
min = math.inf
sum = 0
firstHeap = []
secondHeap = []
numDic = {}

n = int(input().rstrip())

for _ in range(n):
  num = int(input().rstrip())

  sum += num

  if num > max:
    max = num

  if num < min:
    min = num

  if num in numDic:
    numDic[num] += 1
  else:
    numDic[num] = 1

  if numDic[num] > maxCount:
    maxCount = numDic[num]
    maxCountNumArray = [num]
  elif numDic[num] == maxCount:
    maxCountNumArray.append(num)

  if len(firstHeap) != len(secondHeap):
    if num < -firstHeap[0]:
      heapq.heappush(secondHeap, -heapq.heappop(firstHeap))
      heapq.heappush(firstHeap, -num)
    else:
      heapq.heappush(secondHeap, num)
  else:
    if len(firstHeap) == 0 or num < secondHeap[0]:
      heapq.heappush(firstHeap, -num)
    else:
      heapq.heappush(firstHeap, -heapq.heappop(secondHeap))
      heapq.heappush(secondHeap, num)

print(round(sum / n))
print(-firstHeap[0])
print(maxCountNumArray[0] if len(maxCountNumArray) == 1 else sorted(maxCountNumArray)[1])
print(max - min)