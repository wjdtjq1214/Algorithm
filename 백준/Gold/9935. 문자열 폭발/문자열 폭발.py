result = []

string = input()
word = input()

for i in range(len(string)):
  char = string[i]

  result.append(char)

  if len(result) < len(word):
    continue

  if char == word[-1]:
    flag = True

    for i in range(len(word)):
      if word[-(i + 1)] != result[-(i + 1)]:
        flag = False
        break

    if flag:
      for _ in range(len(word)):
        result.pop()

print(''.join(result) if len(result) != 0 else 'FRULA')