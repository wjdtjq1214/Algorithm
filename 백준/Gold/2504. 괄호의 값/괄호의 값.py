stack = []
flag = True

word = input()

for i in range(len(word)):
  num = 0

  if word[i] == '(' or word[i] == '[':
    stack.append(word[i])
  else:
    while len(stack) != 0 and type(stack[-1]) == int:
      num += stack.pop()
      
    if word[i] == ')':
      if len(stack) == 0 or stack[-1] != '(':
        print('0')
        flag = False
        break
      else:
        stack.pop()

      stack.append(2 if num == 0 else num * 2)
    elif word[i] == ']':
      if len(stack) == 0 or stack[-1] != '[':
        print('0')
        flag = False
        break
      else:
        stack.pop()

      stack.append(3 if num == 0 else num * 3)

if flag:
  result = 0

  for stackValue in stack:
    if type(stackValue) == str:
      print('0')
      flag = False
      break

    result += stackValue

  if flag:
    print(result)