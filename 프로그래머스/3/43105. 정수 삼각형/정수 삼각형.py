def solution(triangle):
    for i in range(len(triangle)):
        if i == 0:
            print("pass")
            continue
                   
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][0]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][-1]
            else:
                triangle[i][j] += triangle[i - 1][j - 1] if triangle[i - 1][j - 1] > triangle[i - 1][j] else triangle[i - 1][j]
            
            
    return max(triangle[-1])
                   
    
            