resultNumDown = 1

numUp1, numDown1 = map(int, input().split())
numUp2, numDown2 = map(int, input().split())

numUp = (numUp1 * numDown2) + (numUp2 * numDown1)
numDown = numDown1 * numDown2

numDownArr = []

while numDown > 1:
  for i in range(2, numDown + 1):
    if numDown % i == 0:
      numDownArr.append(i)
      numDown = numDown // i
      break

for num in numDownArr:
  if numUp % num == 0:
    numUp = numUp // num
  else:
    resultNumDown *= num

print(str(numUp) + ' ' + str(resultNumDown))