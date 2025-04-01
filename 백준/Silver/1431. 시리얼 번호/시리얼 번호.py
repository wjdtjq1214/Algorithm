import sys

wordArr = []

count = int(input())

for _ in range(count):
  wordSum = 0

  word = sys.stdin.readline().rstrip()

  for index in range(len(word)):
    char = word[index]

    if ord(char) >= 48 and ord(char) <= 57:
      wordSum += int(char)

  wordArr.append({
    'word': word,
    'wordSum': wordSum
  })

wordArr.sort(key = lambda obj: (len(obj['word']), obj['wordSum'], obj['word']))

for wordObj in wordArr:
  print(wordObj['word'])