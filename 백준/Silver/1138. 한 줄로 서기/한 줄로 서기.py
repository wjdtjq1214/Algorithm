length = int(input())

result = [0 for _ in range(length)]

countList = list(map(int, input().split()))

for i in range(length):
  zeroCount = 0
  num = i + 1

  j = 0

  while zeroCount < countList[i] or result[j] != 0:
    if result[j] == 0:
      zeroCount += 1

    j += 1

  result[j] = str(num)

print(' '.join(result))