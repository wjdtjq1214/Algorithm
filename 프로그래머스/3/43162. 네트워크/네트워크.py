from collections import deque

def solution(n, computers):
    networkCount = 0
    visitList = [False for _ in range(n)]
    nodeObj = {}
    
    for i in range(n):
        nodeList = []
        
        for j in range(n):
            if i == j:
                continue
                
            if computers[i][j] == 1:
                nodeList.append(j)
                
        if len(nodeList) == 0:
            visitList[i] = True
            networkCount += 1
        else:
            nodeObj[i] = nodeList
            
    for i in nodeObj:
        if visitList[i]:
            continue
            
        networkCount += 1
        queue = deque([i])
        
        while len(queue) > 0:
            first = queue.popleft()
            visitList[first] = True
            
            for j in nodeObj[first]:
                if not visitList[j]:
                    queue.append(j)
                        
    return networkCount
    