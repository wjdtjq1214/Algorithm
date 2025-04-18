import sys

input = sys.stdin.readline

result = 0
obj = {}

count = int(input().rstrip())

for _ in range(count):
  inputString = input().rstrip()

  if inputString == 'ENTER':
    obj = {}
    continue

  if inputString not in obj:
    obj[inputString] = True
    result += 1
  
print(result)