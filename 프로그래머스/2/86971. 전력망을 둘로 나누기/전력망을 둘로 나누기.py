import math
from collections import deque

def solution(n, wires):
    result = math.inf
    
    for i in range(len(wires)):
        queue = deque()
        count = 0
        wireList = wires[:i] + wires[i + 1:]
        nodeObj = {}
        visitedList = [False] * (n + 1)
        
        for [start, end] in wireList:
            if start in nodeObj:
                nodeObj[start].append(end)
            else:
                nodeObj[start] = [end]
                
            if end in nodeObj:
                nodeObj[end].append(start)
            else:
                nodeObj[end] = [start]
                
        keyList = list(nodeObj.keys())
        queue.append(keyList[0])
                
        while len(queue) > 0:
            first = queue.popleft()
            visitedList[first] = True
            count += 1
            
            for node in nodeObj[first]:
                if not visitedList[node]:
                    queue.append(node)
                    
        result = min(result, abs(n - count * 2))
        
    return result