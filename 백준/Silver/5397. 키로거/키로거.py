length = int(input())

for _ in range(length):
  pwStack = []
  preStack = []

  wordArr = list(input())

  for word in wordArr:
    if word == '<':
      if len(pwStack) > 0:
        preStack.append(pwStack.pop())
    elif word == '>':
      if len(preStack) > 0:
        pwStack.append(preStack.pop())
    elif word == '-':
      if len(pwStack) > 0:
        pwStack.pop()
    else:
      pwStack.append(word)

  while len(preStack) > 0:
    pwStack.append(preStack.pop())
    
  print(''.join(pwStack))