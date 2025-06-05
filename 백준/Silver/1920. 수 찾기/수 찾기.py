numDic = {}

input()

for num in input().split():
  if num in numDic:
    numDic[num] += 1
  else:
    numDic[num] = 1

input()

for num in input().split():
  if num in numDic:
    print(1)
  else:
    print(0)