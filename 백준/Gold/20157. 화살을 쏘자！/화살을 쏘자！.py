import sys

input = sys.stdin.readline

ratioObj = {}

count = int(input())

for _ in range(count):
  ratio = None

  x, y = map(int, input().split())

  if x == 0:
    if y > 0:
      ratio = 'x0y+'
    else:
      ratio = 'x0y-'
  elif y == 0:
    if x > 0:
      ratio = 'x+y0'
    else:
      ratio = 'x-y0'
  else:
    ratio = x / y

    if x > 0 and y > 0:
      ratio = f'+x+y{ratio}'
    elif x < 0 and y > 0:
      ratio = f'-x+y{abs(ratio)}'
    elif x < 0 and y < 0:
      ratio = f'-x-y{ratio}'
    elif x > 0 and y < 0:
      ratio = f'+x-y{abs(ratio)}'

  if ratio in ratioObj:
    ratioObj[ratio] += 1
  else:
    ratioObj[ratio] = 1

maxCount = max(ratioObj.values())

print(maxCount)