sumArr = []
sum = 0

input()

numArr = list(map(int, input().split()))

for i in range(len(numArr)):
  num = numArr[i]  

  if sum + num > 0:
    if num < 0:
      sumArr.append(sum)

    sum += num
  else:
    sumArr.append(sum)
    sum = 0

  if i == len(numArr) - 1:
    sumArr.append(sum)


sumMax = max(sumArr)

print(sumMax if sumMax > 0 else max(numArr))