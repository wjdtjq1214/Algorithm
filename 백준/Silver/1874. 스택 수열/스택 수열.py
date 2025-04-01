stack = []
resultArr = []

length = int(input())

arr = [i for i in range(length, 0, -1)]

for _ in range(length):
  num = int(input())

  while (len(stack) == 0 or stack[-1] != num) and len(arr) > 0:
    stack.append(arr.pop())
    resultArr.append('+')

  if stack[-1] == num:
    stack.pop()
    resultArr.append('-')
  else:
    print('NO')
    break

if len(stack) == 0:
  for result in resultArr:
    print(result)