function solution(number, k) {
    let i = 0
    let numArray = []
    
    while (i < number.length) {
        if (numArray.length === 0) {
            numArray.push(number[i])
            i++
            continue
        }
        
        if (k > 0 && numArray[numArray.length - 1] < number[i]) {
            k--
            numArray.pop()
            continue
        }
        
        numArray.push(number[i])
        i++
    }
    
    if (k > 0) {
        numArray = numArray.slice(0, numArray.length - k)
    }
    
    return numArray.join('')
}