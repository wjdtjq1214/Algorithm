function solution(weights) {
    let result = 0
    const weightObj = {}
    const ratioArray = [1, 2 / 3, 1 / 2, 3 / 2, 3 / 4, 2, 4 / 3]
    
    for (const weight of weights) {
        if (weightObj[weight]) weightObj[weight]++
        else weightObj[weight] = 1
    }
    
    for (const weight of weights) {
        for (const ratio of ratioArray) {
            result += weightObj[weight * ratio]?? 0
        }
        result--
    }
    
    return result / 2
}