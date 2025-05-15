function solution(data, col, row_begin, row_end) {
    let result = 0
    
    data.sort((a, b) => {
        if (a[col - 1] === b[col - 1]) {
            return b[0] - a[0]
        } else {
            return a[col - 1] - b[col - 1]
        }
    })
    
    for (let i = row_begin - 1; i < row_end; i++) {
        let value = 0
        
        for (const num of data[i]) {
            value += num % (i + 1)
        }
        
        result ^= value
    }
    
    return result
}