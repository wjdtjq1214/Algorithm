def solution(n, s):
    returnValue = []
    
    avgValue = s // n
    overCount = s % n
    
    if avgValue == 0:
        returnValue.append(-1)
    else:
        for _ in range(n - overCount):
            returnValue.append(avgValue)
            
        for _ in range(overCount):
            returnValue.append(avgValue + 1)
    
    return returnValue