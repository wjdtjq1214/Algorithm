function solution(storey) {
    let result = 0
    
    for (let i = 0; storey > 0; i++) {
        const num = storey % (10 ** (i + 1))
        
        if (num > 5 * (10 ** i)) {
            result += ((10 ** (i + 1)) - num) / (10 ** i)
            storey += (10 ** (i + 1)) - num
        } else if (num === 5 * (10 ** i)) {
            const nextNum = storey % (10 ** (i + 2))
            
            if (nextNum >= 5 * (10 ** (i + 1))) {
                result += ((10 ** (i + 1)) - num) / (10 ** i)
                storey += (10 ** (i + 1)) - num
            } else {
                result += num / (10 ** i)
                storey -= num
            }
        } else {
            result += num / (10 ** i)
            storey -= num
        }
    }
    
    return result
}