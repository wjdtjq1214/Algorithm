from collections import deque

length, count = map(int, input().split())
indexArr = map(int, input().split())
totalCount = 0
size = length

queue = deque([i for i in range(1, length + 1)])

for i in indexArr:
  popCount = 0

  first = queue.popleft()

  while first != i:
    queue.append(first)
    first = queue.popleft()
    popCount += 1

  if popCount > size - popCount:
    totalCount += size - popCount
  else:
    totalCount += popCount
  
  size -= 1

print(totalCount)