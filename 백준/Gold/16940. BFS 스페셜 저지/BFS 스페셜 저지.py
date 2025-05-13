from collections import deque
import sys

input = sys.stdin.readline

edgeCount = int(input())

flag = True
queue = deque(['1'])
graphObj = {}
visited = [False] * (edgeCount + 1)
visited[1] = True

for _ in range(edgeCount - 1):
  [start, end] = input().split()

  if start in graphObj:
    graphObj[start].append(end)
  else:
    graphObj[start] = [end]

  if end in graphObj:
    graphObj[end].append(start)
  else:
    graphObj[end] = [start]

inputResultList = input().split()
inputResultQueue = deque(inputResultList)

if inputResultQueue.popleft() != '1':
  print(0)
  flag = False

while len(queue) > 0 and flag:
  first = queue.popleft()

  if graphObj[first]:
    nextObj = {}

    for edge in graphObj[first]:
      if not visited[int(edge)]:
        nextObj[edge] = True

    while len(nextObj) > 0 and flag:
      inputResult = inputResultQueue.popleft()

      if inputResult not in nextObj:
        flag = False
        print(0)
        break

      visited[int(inputResult)] = True
      queue.append(inputResult)
      del nextObj[inputResult]

if flag:
  print(1)