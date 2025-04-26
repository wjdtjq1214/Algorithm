from collections import deque

def solution(queue1, queue2):
    maxLength = len(queue1) * 4
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    result = 0
    totalSum = 0
    queue1Sum = 0
    queue2Sum = 0
    max = 0
    min = 0
    
    for i in range(len(queue1)):
        queue1Num = queue1[i]
        queue2Num = queue2[i]
        max = queue1Num if max < queue1Num else max
        max = queue2Num if max < queue2Num else max
        min = queue1Num if min > queue1Num else min
        min = queue2Num if min > queue2Num else min
        queue1Sum += queue1Num
        queue2Sum += queue2Num
        
    totalSum = queue1Sum + queue2Sum
    
    if totalSum % 2 != 0 or max > totalSum / 2 or max + min > totalSum / 2:
        return -1

    while queue1Sum != queue2Sum:
        if result > maxLength:
            break
            
        if queue1Sum > queue2Sum:
            value = queue1.popleft()
            queue1Sum -= value
            queue2Sum += value
            
            queue2.append(value)
        else:
            value = queue2.popleft()
            queue2Sum -= value
            queue1Sum += value
            
            queue1.append(value)
        
        result += 1
    
    return -1 if maxLength < result else result