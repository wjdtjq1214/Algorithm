result = 0

h, w = map(int, input().split())
tallList = list(map(int, input().split()))

maxH = max(tallList)

for i in range(maxH):
  index = None

  for j in range(len(tallList)):
    if maxH - i <= tallList[j]:
      if index != None:
        result += j - index - 1

      index = j

print(result)