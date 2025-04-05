function solution(order) {
    const length = order.length
    const mainArr = order.map((num, i) => i + 1)
    let result = 0
    let lastIndex = null
    
    for (const i of order) {
        const iIndex = i + 1
        
        if (lastIndex == null || iIndex > lastIndex) {
            lastIndex = iIndex
            result++
            mainArr[iIndex] = null
        } else {
            if (mainArr.slice(iIndex + 1, lastIndex).filter((num) => num !== null).length !== 0) break
            else {
                lastIndex = iIndex
                result++
                mainArr[iIndex] = null
            }
        }
    }
    
    return result
}