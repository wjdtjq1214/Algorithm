intStr = input()

countList = [0 for _ in range(len(intStr) + 1)]
countList[0] = 1

for i in range(1, len(intStr) + 1):
  if i == 1:
    countList[i] = countList[i - 1]
  elif int(intStr[i - 1]) == 0 and (int(intStr[i - 2]) == 0 or int(intStr[i - 2]) > 3):
    print(0)
    exit()
  elif int(intStr[i - 1]) == 0:
    countList[i] = countList[i - 2]
  elif int(intStr[i - 2: i]) > 34 or int(intStr[i - 2]) == 0:
    countList[i] = countList[i - 1]
  else:
    countList[i] = countList[i - 1] + countList[i - 2]
  

print(countList[-1])