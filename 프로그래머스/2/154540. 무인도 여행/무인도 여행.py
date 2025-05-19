from collections import deque

def solution(maps):
    checkList = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    sumList = []
    queue = deque()
    randObj = {}
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                randObj[i, j] = maps[i][j]
    
    while len(randObj) > 0:
        start = list(randObj.keys())[0]
        queue.append(start)
        sum = int(randObj[start])
        del randObj[start]
        
        while len(queue) > 0:
            first = queue.popleft()
            
            for [x, y] in checkList:
                if (first[0] + x, first[1] + y) in randObj:
                    queue.append([first[0] + x, first[1] + y])
                    sum += int(randObj[first[0] + x, first[1] + y])
                    del randObj[first[0] + x, first[1] + y]
                    
        sumList.append(sum)
        
    if len(sumList) == 0:
        return [-1]
    
    sumList.sort()
    
    return sumList