from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    checkList = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visitList = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([[0, 0]])
    visitList[0][0] = True
    
    while len(queue) > 0:
        first = queue.popleft()
        
        for i in range(4):
            x = first[0] + checkList[i][0]
            y = first[1] + checkList[i][1]
            
            if x >= 0 and x < n and y >= 0 and y < m and visitList[x][y] == False and maps[x][y] != 0:
                queue.append([x, y])
                visitList[x][y] = True
                maps[x][y] = maps[first[0]][first[1]] + 1
                
    return -1 if maps[n - 1][m - 1] == 1 else maps[n - 1][m - 1]
    
    