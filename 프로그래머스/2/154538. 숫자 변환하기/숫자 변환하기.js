function solution(x, y, n) {
    const countArr = [0]
    
    for (let i = x + 1; i <= y; i++) {
        let minCount = null
        
        if (i - n - x >= 0)
            minCount = countArr[i - n - x]
        
        if (i % 2 === 0
            && i / 2 >= x
            && countArr[(i / 2) - x] !== null
            && (minCount === null || minCount > countArr[(i / 2) - x]))
            minCount = countArr[(i / 2) - x]
        
        if (i % 3 === 0
            && i / 3 >= x
            && countArr[(i / 3) - x] !== null
            && (minCount === null || minCount > countArr[(i / 3) - x]))
            minCount = countArr[(i / 3) - x]
        
        countArr.push(minCount !== null? minCount + 1: null)
    }
    
    return countArr[y - x] === null? -1: countArr[y - x]
}