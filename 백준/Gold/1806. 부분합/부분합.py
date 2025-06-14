count, target = map(int, input().split())

numberList = list(map(int, input().split()))

start = 0
end = 0
sum = 0
result = 0

while end < count:
  sum += numberList[end]

  while sum - numberList[start] >= target and start < end:
    sum -= numberList[start]
    start += 1

  if (result == 0 or end - start + 1 < result) and sum >= target:
    result = end - start + 1

  end += 1

print(result)