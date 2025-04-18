import sys

input = sys.stdin.readline
objList = []

word = input().rstrip()

for i in range(len(word)):
  char = word[i]
  newObj = {} if i == 0 else objList[i - 1].copy()

  if char in newObj:
    newObj[char] += 1
  else:
    newObj[char] = 1

  objList.append(newObj)

count = int(input().rstrip())

for _ in range(count):
  char, start, end = input().strip().split()

  if start == '0':
    if char in objList[int(end)]:
      print(objList[int(end)][char])
    else:
      print(0)
  else:
    if char not in objList[int(end)]:
      print(0)
    else:
      if char not in objList[int(start) - 1]:
        print(objList[int(end)][char])
      else:
        print(objList[int(end)][char] - objList[int(start) - 1][char])