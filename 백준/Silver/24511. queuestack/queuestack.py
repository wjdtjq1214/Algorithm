import sys
from collections import deque

input = sys.stdin.readline

result = []
queueStackCount = int(input())
kindList = input().split()
initList = input().split()
numCount = int(input())
numList = input().split()
queueStackDeque = deque()

for i in range(queueStackCount):
  if kindList[i] == '0':
    queueStackDeque.appendleft(initList[i])

for num in numList:
  queueStackDeque.append(num)
  result.append(queueStackDeque.popleft())

print(' '.join(result))