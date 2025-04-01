def solution(n, works):    
    if sum(works) <= n:
        return 0
    
    countList = []
    
    distinctWorkList = list(set(works))
    distinctWorkList.sort(reverse = True)
    
    for num in distinctWorkList:
        countList.append(works.count(num))
        
    while n > 0:
        thisWorkHour = distinctWorkList[0]
        thisWorkCount = countList[0]
        
        if len(distinctWorkList) == 1:
            minusValue = n // thisWorkCount
            remainValue = n % thisWorkCount
            
            del distinctWorkList[0]
            del countList[0]
            
            if minusValue > 0:
                distinctWorkList.insert(0, thisWorkHour - minusValue)
                distinctWorkList.insert(1, thisWorkHour - minusValue - 1)
            else:
                distinctWorkList.insert(0, thisWorkHour)
                distinctWorkList.insert(1, thisWorkHour - 1)
            
            countList.insert(0, thisWorkCount - remainValue)
            countList.insert(1, remainValue)
            
            break
        else:
            minusWorkValue = thisWorkHour - distinctWorkList[1]
            needWorkValue  = minusWorkValue * thisWorkCount
            
            if needWorkValue > n:
                minusValue = n // thisWorkCount
                remainValue = n % thisWorkCount

                del distinctWorkList[0]
                del countList[0]

                if minusValue > 0:
                    distinctWorkList.insert(0, thisWorkHour - minusValue)
                    countList.insert(0, thisWorkCount - remainValue)
                    
                    if thisWorkHour - minusValue - 1 != distinctWorkList[1]:
                        distinctWorkList.insert(1, thisWorkHour - minusValue - 1)
                        countList.insert(1, remainValue)
                    else: 
                        countList[1] += remainValue
                else:
                    distinctWorkList.insert(0, thisWorkHour)
                    countList.insert(0, thisWorkCount - remainValue)
                    
                    if thisWorkHour - 1 != distinctWorkList[1]:
                        distinctWorkList.insert(1, thisWorkHour - 1)
                        countList.insert(1, remainValue)
                    else:
                        countList[1] += remainValue
                        
                break
            else:
                del distinctWorkList[0]
                del countList[0]
                
                countList[0] += thisWorkCount
                n -= needWorkValue
    
    sumValue = 0
    
    for i in range(len(distinctWorkList)):
        sumValue += pow(distinctWorkList[i], 2) * countList[i]
    
    return sumValue