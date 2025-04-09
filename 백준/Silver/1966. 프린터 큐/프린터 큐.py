from collections import deque

queueCount = int(input())

for _ in range(queueCount):
  count = 0
  nodeCount, index = map(int, input().split())
  numList = list(map(int, input().split()))

  queue = deque([{
    "num": numList[i],
    "index": i
  } for i in range(nodeCount)])
  numList.sort()

  while True:
    node = queue.popleft()

    if node["num"] == numList[-1]:
      numList.pop()
      count += 1

      if node["index"] == index:
        print(count)
        break
    else:
      queue.append(node)