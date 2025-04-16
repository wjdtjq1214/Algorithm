numObj = {}
sum = 0
result = 0

n, m = map(int, input().split())
numList = list(map(int, input().split()))

for i in range(n):
  sum += numList[i]
  remainder = sum % m

  if remainder == 0:
    if remainder in numObj:
      numObj[remainder] += 1
    else:
      numObj[remainder] = 1
    
    result += numObj[remainder]
  else:
    if remainder in numObj:
      result += numObj[remainder]
      numObj[remainder] += 1
    else:
      numObj[remainder] = 1

print(result)