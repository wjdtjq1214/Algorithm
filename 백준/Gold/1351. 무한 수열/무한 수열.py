import math

n, p, q = map(int, input().split())

numDic = {
  0: 1,
  1: 2
}

def getNum(num):
  if num in numDic:
    return numDic[num]
  
  numDic[num] = getNum(math.floor(num / p)) + getNum(math.floor(num / q))
  return numDic[num]

print(getNum(n))