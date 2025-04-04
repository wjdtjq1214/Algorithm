result = 0

length = int(input())

arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))

arrA.sort()
arrB.sort(reverse=True)

for i in range(length):
  result += (arrA[i] * arrB[i])

print(result)