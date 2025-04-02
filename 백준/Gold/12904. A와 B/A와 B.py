inputStr = input()
targetStr = input()

while len(inputStr) != len(targetStr):
  if targetStr[len(targetStr) - 1] == 'A':
    targetStr = targetStr[:len(targetStr) - 1]
  else:
    targetStr = ''.join(reversed(targetStr[:len(targetStr) - 1]))

if inputStr == targetStr:
  print(1)
else:
  print(0)