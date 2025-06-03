g, s = map(int, input().split())
w = input()
string = input()

wObj = {}
subObj = {}
result = 0
flag = True
start = 0
end = start + g

for char in w:
  if char in wObj:
    wObj[char] += 1
  else:
    wObj[char] = 1

for i in range(end):
  if string[i] in subObj:
    subObj[string[i]] += 1
  else:
    subObj[string[i]] = 1

for wObjKey in wObj:
  if wObjKey not in subObj or subObj[wObjKey] != wObj[wObjKey]:
    flag = False
    break

if flag:
  result += 1

while end < s:
  flag = True

  if subObj[string[start]] == 1:
    del subObj[string[start]]
  else:
    subObj[string[start]] -= 1

  if string[end] in subObj:
    subObj[string[end]] += 1
  else:
    subObj[string[end]] = 1

  for wObjKey in wObj:
    if wObjKey not in subObj or subObj[wObjKey] != wObj[wObjKey]:
      flag = False
      break

  if flag:
    result += 1

  start += 1
  end += 1

print(result)