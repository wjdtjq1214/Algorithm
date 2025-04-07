word = input()

count = int(input())

for _ in range(count):
  char, start, end = input().split()

  print(word[int(start): int(end) + 1].count(char))