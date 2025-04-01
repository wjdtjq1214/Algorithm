result = 0

arr = input().split('-')

for i in range(len(arr)):
  if i == 0:
    result += sum(list(map(int, arr[i].split('+'))))
  else:
    result -= sum(list(map(int, arr[i].split('+'))))

print(result)