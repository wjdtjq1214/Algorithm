from collections import deque

length = int(input())

for _ in range(length):
  flag = True
  funcStr = input()
  arrLen = int(input())
  strArr = input().split(',')
  queue = deque()

  deleteCount = funcStr.count('D')

  if arrLen < deleteCount:
    print('error')
    continue
  elif arrLen == deleteCount:
    print('[]')
    continue

  if (arrLen == 1):
    queue.append(strArr[0][1:len(strArr[0]) - 1])
  elif (arrLen != 0):
    for i in range(arrLen):
      if i == 0:
        queue.append(strArr[i][1:len(strArr[i])])
      elif i == arrLen - 1:
        queue.append(strArr[i][0:len(strArr[i]) - 1])
      else:
        queue.append(strArr[i])

  for funcWord in funcStr:
    if funcWord == 'R':
      flag = False if flag else True
    elif funcWord == 'D':
      if flag:
        queue.popleft()
      else:
        queue.pop()

  if not flag:
    queue.reverse()

  print('[' + ','.join(queue) + ']')