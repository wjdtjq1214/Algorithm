from collections import deque
import sys

input = sys.stdin.readline

numDequeue = deque()

n, l = map(int, input().split())
numList = list(map(int, input().split()))

for i in range(n):
  num = numList[i]

  while numDequeue and numDequeue[-1][1] > num:
    numDequeue.pop()

  numDequeue.append((i, num))

  if numDequeue[0][0] == i - l:
    numDequeue.popleft()

  print(numDequeue[0][1])