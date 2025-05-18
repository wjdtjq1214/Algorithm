from collections import deque
import math

def solution(maps):
    firstMapList = []
    secondMapList = []
    startPoint = []
    endPoint = []
    leverPoint = []
    checkList = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    
    for i in range(len(maps)):
        mapStr = maps[i]
        subMapList = []
        
        for j in range(len(mapStr)):
            if mapStr[j] == 'S':
                startPoint = [i, j]
            elif mapStr[j] == 'E':
                endPoint = [i, j]
            elif mapStr[j] == 'L':
                leverPoint = [i, j]
            
            subMapList.append(-1 if mapStr[j] == 'X' else math.inf)
                
        firstMapList.append(subMapList)
        secondMapList.append(subMapList.copy())    
        
    firstMapList[startPoint[0]][startPoint[1]] = 0
    secondMapList[leverPoint[0]][leverPoint[1]] = 0
    
    queue = deque([startPoint])
    
    while len(queue) > 0:
        first = queue.popleft()
        
        for [x, y] in checkList:
            if 0 <= first[1] + x < len(maps[0]) and 0 <= first[0] + y < len(maps) and firstMapList[first[0] + y][first[1] + x] != -1 and firstMapList[first[0]][first[1]] + 1 < firstMapList[first[0] + y][first[1] + x]:
                firstMapList[first[0] + y][first[1] + x] = firstMapList[first[0]][first[1]] + 1
                queue.append([first[0] + y, first[1] + x])
                
    queue = deque([leverPoint])
    
    while len(queue) > 0:
        first = queue.popleft()
        
        for [x, y] in checkList:
            if 0 <= first[1] + x < len(maps[0]) and 0 <= first[0] + y < len(maps) and secondMapList[first[0] + y][first[1] + x] != -1 and secondMapList[first[0]][first[1]] + 1 < secondMapList[first[0] + y][first[1] + x]:
                secondMapList[first[0] + y][first[1] + x] = secondMapList[first[0]][first[1]] + 1
                queue.append([first[0] + y, first[1] + x])
    
    if firstMapList[leverPoint[0]][leverPoint[1]] == math.inf or secondMapList[endPoint[0]][endPoint[1]] == math.inf:
        return -1
    else:
        return firstMapList[leverPoint[0]][leverPoint[1]] + secondMapList[endPoint[0]][endPoint[1]]