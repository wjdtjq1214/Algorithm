from collections import deque

def solution(n, vertex):
    max = 0
    queue = deque([1])
    countList = [0]
    edgeObj = {}
    visitObj = {}
    
    for i in range(1, n + 1):
        visitObj[i] = False
        countList.append(None)
        
    countList[1] = 1
    
    for [start, end] in vertex:
        if start in edgeObj:
            edgeObj[start].append(end)
        else:
            edgeObj[start] = [end]
            
        if end in edgeObj:
            edgeObj[end].append(start)
        else:
            edgeObj[end] = [start]
        
    while len(queue) > 0:
        first = queue.popleft()
        visitObj[first] = True
        
        for edge in edgeObj[first]:
            if not visitObj[edge] and (countList[edge] == None or countList[edge] > countList[first] + 1):
                queue.append(edge)
                countList[edge] = countList[first] + 1
                max = countList[edge] if countList[edge] > max else max
                
    return countList.count(max)
    