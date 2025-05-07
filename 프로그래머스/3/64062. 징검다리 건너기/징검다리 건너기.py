from collections import deque

def solution(stones, k):
    dequeue = deque()
    minValue = None
    
    for i in range(k):            
        while len(dequeue) > 0 and dequeue[-1][1] <= stones[i]:
            dequeue.pop()
            
        dequeue.append([i, stones[i]])
    
    for i in range(k, len(stones) + 1):        
        if dequeue[0][0] < i - k:
            dequeue.popleft()

        minValue = dequeue[0][1] if minValue == None or minValue > dequeue[0][1] else minValue
        
        if i == len(stones):
            break
        
        while len(dequeue) > 0 and dequeue[-1][1] <= stones[i]:
            dequeue.pop()
            
        dequeue.append([i, stones[i]])        
        
    return minValue