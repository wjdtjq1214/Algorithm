word = input()

countList = [0] * (len(word) + 1)
countList[0] = 1

for i in range(1, len(word) + 1):
  if word[i - 1] != '0':
    countList[i] += countList[i - 1]
  elif i == 1 or int(word[i - 2]) > 3:
    print(0)
    exit()

  if i > 1 and 10 <= int(word[i - 2: i]) <= 26:
    countList[i] += countList[i - 2]

print(countList[-1] % 1000000)