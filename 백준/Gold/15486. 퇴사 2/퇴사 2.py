import sys

input = sys.stdin.readline

n = int(input())

numList = [0 for _ in range(n + 1)]
maxValue = 0

for i in range(n):
  maxValue = maxValue if maxValue > numList[i] else numList[i]

  t, p = map(int, input().split())

  if i + t > n:
    continue

  newValue = maxValue + p

  numList[i + t] = newValue if newValue > numList[i + t] else numList[i + t]

print(max(numList))