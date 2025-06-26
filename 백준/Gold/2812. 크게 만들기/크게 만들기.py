numStack = []

n, k = map(int, input().split())
numStr = input()

for i in range(n):
  while len(numStack) > 0 and k > 0 and numStack[-1] < numStr[i]:
    numStack.pop()
    k -= 1

  numStack.append(numStr[i])

if k > 0:
  numStack = numStack[:-k]

print(''.join(numStack))