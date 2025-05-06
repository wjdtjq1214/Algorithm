function solution(n, lost, reserve) {
    const lostArr = []
    const reserveObj = {}
    let finalLostCount = 0
    
    for (const reserveNum of reserve) reserveObj[reserveNum] = true
    
    for (const lostNum of lost) {
        if (reserveObj[lostNum])
            reserveObj[lostNum] = false
        else
            lostArr.push(lostNum)
    }
    
    lostArr.sort((a, b) => a - b)
    
    for (const lostNum of lostArr) {
        if (reserveObj[lostNum - 1]?? false == true) reserveObj[lostNum - 1] = false
        else if (reserveObj[lostNum + 1]?? false == true) reserveObj[lostNum + 1] = false
        else finalLostCount++
    }
    
    return n - finalLostCount
}
