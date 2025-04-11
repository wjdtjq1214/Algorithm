from collections import deque

def solution(sequence, k):
    min = None
    resultList = []
    queue = deque()
    sumValue = 0
    
    for i in range(len(sequence)):
        queue.append(sequence[i])
        sumValue += sequence[i]
        
        if sumValue < k:
            continue
        
        while k < sumValue:
            sumValue -= queue.popleft()
            
        if sumValue == k:
            resultList.append([len(queue), [i - len(queue) + 1,i]])
            
            if min == None or min > len(queue):
                min = len(queue)
            
    for subList in resultList:
        if subList[0] == min:
            return subList[1]
        