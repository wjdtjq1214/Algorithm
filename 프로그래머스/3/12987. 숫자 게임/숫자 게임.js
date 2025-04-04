function solution(a, b) {
    let score = 0
    
    a.sort((a, b) => b - a)
    b.sort((a, b) => b - a)
    
    let aIndex = 0
    let bIndex = 0
    
    while (aIndex < a.length) {
        if (a[aIndex] < b[bIndex]) {
            score++
            bIndex++
        }
        
        aIndex++
    }
    
    return score
}