function solution(n) {
    const numArray = []
    const numObj = {
        1: 1,
        2: 2,
        3: 4
    }
    
    while (n > 0) {
        if (n % 3 == 0) {
            numArray.push(numObj[3])
            n = n / 3 - 1
        } else {
            numArray.push(numObj[n % 3])
            n = Math.floor(n / 3)
        }
    }
    
    return numArray.reverse().join('')
}