countList = [0 for _ in range(11)]

countList[0] = 1

for i in range(1, 11):
  if i - 1 >= 0:
    countList[i] += countList[i - 1]
  
  if i - 2 >= 0:
    countList[i] += countList[i - 2]

  if i - 3 >= 0:
    countList[i] += countList[i - 3]

t = int(input().rstrip())

for _ in range(t):
  n = int(input().rstrip())
  
  print(countList[n])