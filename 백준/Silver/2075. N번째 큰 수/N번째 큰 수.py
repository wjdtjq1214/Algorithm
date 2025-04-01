totalArr = []

length = int(input())

for _ in range(length):
  arr = list(map(int, input().split()))
  arr.sort(reverse = True)

  if len(totalArr) == 0:
    totalArr = arr
    continue

  arr2 = totalArr
  totalArr = []

  i = 0
  j = 0

  while True:
    if len(totalArr) >= length:
      break
    elif arr[i] >= arr2[j]:
      totalArr.append(arr[i])
      i += 1
    else:
      totalArr.append(arr2[j])
      j += 1

print(totalArr[-1])