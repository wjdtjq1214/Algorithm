length, maxWeight = map(int, input().split())

weigthValiuLst = [0 for _ in range(maxWeight + 1)]
indexObjList = [{} for _ in range(maxWeight + 1)]
itemList = []

for _ in range(length):
  weight, value = map(int, input().split())
  itemList.append([weight, value])

for i in range(1, maxWeight + 1):
  for j in range(length):
    item = itemList[j]

    if i - item[0] >= 0 and j not in indexObjList[i - item[0]] and weigthValiuLst[i - item[0]] + item[1] > weigthValiuLst[i]:
      indexObjList[i] = indexObjList[i - item[0]].copy()
      indexObjList[i][j] = True
      weigthValiuLst[i] = weigthValiuLst[i - item[0]] + item[1]


print(max(weigthValiuLst))