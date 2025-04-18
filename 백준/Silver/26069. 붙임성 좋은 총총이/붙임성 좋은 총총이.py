import sys

input = sys.stdin.readline

obj = {
  'ChongChong': True
}

count = int(input().rstrip())

for _ in range(count):
  name1, name2 = input().rstrip().split()

  if name1 in obj or name2 in obj:
    obj[name1] = True
    obj[name2] = True

print(len(obj))