function solution(numbers) {
    return numbers.map((num) => {
        let numStr = num.toString(2).split('')
        const last0Index = numStr.lastIndexOf('0')
        
        if (last0Index === -1) {
            numStr[0] = '0'
            numStr = ['1', ...numStr]
        } else {
            numStr[last0Index] = '1'
            
            if (last0Index !== numStr.length - 1) numStr[last0Index + 1] = '0'
        }
        
        return parseInt(numStr.join(''), 2)
    })
}