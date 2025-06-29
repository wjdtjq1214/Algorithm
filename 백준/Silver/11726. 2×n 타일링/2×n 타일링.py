n = int(input().rstrip())

countList = [0 for _ in range(n + 1)]

countList[0] = 1

for i in range(1, n + 1):
  if i == 1:
    countList[i] = countList[i - 1] % 10007

    continue

  countList[i] = (countList[i - 1] + countList[i - 2]) % 10007

print(countList[n])