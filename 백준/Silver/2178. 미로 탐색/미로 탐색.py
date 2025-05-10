from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

checkList = [[-1, 0], [1, 0], [0, -1], [0, 1]]
queue = deque([[0, 0]])
mapList = []
visitList = [[False] * m for _ in range(n)]
visitList[0][0] = True

for _ in range(n):
  inputList = list(map(int, list(input().rstrip())))
  mapList.append(inputList)

while len(queue) > 0:
  x, y = queue.popleft()

  for i in range(4):
    newX = x + checkList[i][0]
    newY = y + checkList[i][1]

    if 0 <= newX < n and 0 <= newY < m and not visitList[newX][newY] and mapList[newX][newY] != 0:
      visitList[newX][newY] = True
      mapList[newX][newY] = mapList[x][y] + 1
      queue.append([newX, newY])

print(mapList[n-1][m-1])