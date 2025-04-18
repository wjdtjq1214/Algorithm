import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
numList = list(map(int, input().rstrip().split()))
sumList = []

for i in range(len(numList)):
  sumList.append(numList[i] if i == 0 else sumList[i-1] + numList[i])

for _ in range(m):
  start, end = map(int, input().rstrip().split())

  print(sumList[end - 1] if start == 1 else sumList[end - 1] - sumList[start - 2])