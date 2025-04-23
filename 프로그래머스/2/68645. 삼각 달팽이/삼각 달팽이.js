function solution(n) {
    let lastNum = 0
    let direction = 'D' // 'R', 'U'
    const snailArr = []
    let x = 0, y = 0
    
    for (let i = 1; i <= n; i++) {
        lastNum += i
        snailArr.push((new Array(i)).fill(0))
    }
    
    for (let i = 1; i <= lastNum; i++) {
        snailArr[x][y] = i
        
        if (direction === 'D') {
            if (x === n - 1 || snailArr[x + 1][y] !== 0) {
                direction = 'R'
                y++
                continue
            }
            
            x++
        } else if (direction === 'R') {
            if (y === snailArr[x].length - 1 || snailArr[x][y + 1] !== 0) {
                direction = 'U'
                x--
                y--
                continue
            }
            
            y++
        } else {
            if (x === 0 || snailArr[x - 1][y - 1] !== 0) {
                direction = 'D'
                x++
                continue
            }
            
            x--
            y--
        }
    }
    
    return snailArr.flat()
}