import heapq

def solution(n, k, enemy):
    count = 0
    heap = []
    
    for enemyCount in enemy:
        if n >= enemyCount:
            heapq.heappush(heap, -enemyCount)
            n -= enemyCount
            count += 1
        else:
            if k == 0:
                break
            
            if len(heap) > 0 and -heap[0] > enemyCount:
                n -= heapq.heappop(heap)
                n -= enemyCount
                heapq.heappush(heap, -enemyCount)
            
            k -= 1    
            count += 1
                
    return count