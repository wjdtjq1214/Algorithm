function solution(begin, end) {
    const result = []
    
    for (let i = begin; i <= end; i++) {
        let numArray = []
        
        for (let num = 2; num <= Math.ceil(Math.sqrt(i)); num++) {
            if (i % num === 0) {
                if (i / num <= 10000000) {
                    result.push(i / num)
                    break
                } else numArray.push(num)
            }
        }
        
        if (result.length === i - begin) {
            if (numArray.length > 0) result.push(numArray.pop())
            else if (i === 1) result.push(0)
            else result.push(1)
        }
    }
    
    return result
}