def solution(operations):
    valueList = []
    min = 0
    max = 0
    
    for operateValue in operations:
        flag, value = operateValue.split()
        
        if flag == "I":
            valueList.append(int(value))
            valueList.sort()
        else:
            if len(valueList) <= 0:
                continue
            
            if value == "1":
                del valueList[-1]
            else:
                del valueList[0]
                
    if len(valueList) > 0:
        max = valueList[-1]
        min = valueList[0]
                
    return [max, min]