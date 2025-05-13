import math

def solution(N, road, K):
    result = 0
    countList = [math.inf] * (N + 1)
    countList[1] = 0
    
    for _ in range(N - 1):
        newCountList = countList.copy()
        
        for [start, end, value] in road:
            if countList[start] != math.inf and newCountList[end] > countList[start] + value:
                newCountList[end] = countList[start] + value
                
            if countList[end] != math.inf and newCountList[start] > countList[end] + value:
                newCountList[start] = countList[end] + value
        
        countList = newCountList
        
    for count in countList:
        if count <= K:
            result += 1
            
    return result    