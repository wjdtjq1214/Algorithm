import sys

input = sys.stdin.readline

n,t = map(int, input().split())

timeList = [0 for _ in range(t + 1)]

for _ in range(n):
  newTimeList = timeList.copy()
  time, score = map(int, input().split())

  for i in range(t + 1):
    if i + time <= t:
      newTimeList[i + time] = max(timeList[i + time], timeList[i] + score)

  timeList = newTimeList

print(max(timeList))