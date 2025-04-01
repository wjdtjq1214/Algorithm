def solution(routes):
    routes.sort()
    minRouteArr = []
    
    for routeArr in routes:
        changeFlag = False
        
        if len(minRouteArr) == 0:
            minRouteArr.append(routeArr)
            continue
            
        for i in range(len(minRouteArr)):
            cameraRouteArr = minRouteArr[i]
                       
            if (cameraRouteArr[0] <= routeArr[0] and cameraRouteArr[1] >= routeArr[0]) or (cameraRouteArr[0] <= routeArr[1] and cameraRouteArr[1] >= routeArr[1]) or (routeArr[0] <= cameraRouteArr[0] and routeArr[1] >= cameraRouteArr[0]) or (routeArr[0] <= cameraRouteArr[1] and routeArr[1] >= cameraRouteArr[1]):
                del minRouteArr[i]
                minRouteArr.append([cameraRouteArr[0] if cameraRouteArr[0] >= routeArr[0] else routeArr[0],
                                    cameraRouteArr[1] if cameraRouteArr[1] <= routeArr[1] else routeArr[1]])
                changeFlag = True
                break
        
        if changeFlag == False:
            minRouteArr.append(routeArr)
            
    print(minRouteArr)
            
    return len(minRouteArr)