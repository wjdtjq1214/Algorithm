def solution(n, stations, w):
    stationRange = w * 2 + 1
    stationCount = 0
    
    for i in range(len(stations)):
        stationAddr = stations[i]
        startPoint = stationAddr - w
        
        if i == 0:
            if startPoint > 1:
                count = startPoint - 1
                stationCount += count / stationRange if count % stationRange == 0 else (count // stationRange) + 1
                print(count)
        else:
            undoEndPoint = stations[i - 1] + w
            count = startPoint - undoEndPoint - 1
            
            if count > 0:
                stationCount += count / stationRange if count % stationRange == 0 else (count // stationRange) + 1
                print(count)
                
        if i == len(stations) - 1:
            endPoint = stationAddr + w
            
            if endPoint < n:
                count = n - endPoint
                stationCount += count / stationRange if count % stationRange == 0 else (count // stationRange) + 1
                print(count)
            
    return stationCount