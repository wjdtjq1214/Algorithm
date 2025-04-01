import math

start, end = map(int, input().split())

arr = [i for i in range(end + 1)]

arr[1] = 0

for i in range(2, math.ceil(math.sqrt(end)) + 1):
  if arr[i] == 0:
    continue
  
  for j in range(i + i, len(arr), i):
    arr[j] = 0

for i in range(start, len(arr)):
  if arr[i] != 0:
    print(arr[i])