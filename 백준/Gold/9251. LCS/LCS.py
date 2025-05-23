word1 = input()
word2 = input()

lcsList = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

for i in range(1, len(word2) + 1):
  for j in range(1, len(word1) + 1):
    if word2[i - 1] == word1[j - 1]:
      lcsList[i][j] = lcsList[i - 1][j - 1] + 1
    else:
      lcsList[i][j] = max(lcsList[i - 1][j], lcsList[i][j - 1])

print(lcsList[-1][-1])