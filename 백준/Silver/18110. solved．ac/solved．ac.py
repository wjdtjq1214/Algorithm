import sys

def myRound(num):
  intNum = int(num // 1)

  if num - intNum >= 0.5:
    return intNum + 1
  else:
    return intNum

numArr = []

count = int(sys.stdin.readline())

for _ in range(count):
  numArr.append(int(sys.stdin.readline()))

cutLine = myRound(count * 15 / 100)

if cutLine != 0:
  numArr.sort()
  numArr = numArr[cutLine:len(numArr) - cutLine]

if count == 0:
  print(0)
else:
  print(myRound(sum(numArr) / len(numArr)))