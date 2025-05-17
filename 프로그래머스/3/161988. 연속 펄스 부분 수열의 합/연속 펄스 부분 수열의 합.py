import math

def solution(sequence):
    firstMax = 0
    firstSum = 0
    secondMax = 0
    secondSum = 0
    firstList = []
    secondList = []
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            firstList.append(sequence[i])
            secondList.append(-sequence[i])
        else:
            firstList.append(-sequence[i])
            secondList.append(sequence[i])
    
    if max(firstList) <= 0:
        firstMax = max(firstList)
    else:
        for i in range(len(firstList)):
            if firstSum + firstList[i] < 0:
                firstSum = 0
            else:
                firstSum += firstList[i]
                
            firstMax = max(firstMax, firstSum)
            
    if max(secondList) <= 0:
        secondMax = max(secondList)
    else:
        for i in range(len(secondList)):
            if secondSum + secondList[i] < 0:
                secondSum = 0
            else:
                secondSum += secondList[i]
                
            secondMax = max(secondMax, secondSum)
    
    return max(firstMax, secondMax)