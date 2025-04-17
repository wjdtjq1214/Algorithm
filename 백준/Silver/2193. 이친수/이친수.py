numLength = int(input())

objList = [{
  'zero': 0,
  'one': 0
} for _ in range(numLength)]

objList[0]['one'] = 1

for i in range(1, numLength):
  objList[i]['zero'] = objList[i - 1]['zero'] + objList[i - 1]['one']
  objList[i]['one'] = objList[i - 1]['zero']

print(objList[numLength - 1]['zero'] + objList[numLength - 1]['one'])