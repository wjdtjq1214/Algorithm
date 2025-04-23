function solution(n) {
    const countArr = []
    
    for (let i = 0; i <= n; i++)
        countArr.push(0)
    
    countArr[0] = BigInt(1)
    countArr[1] = BigInt(1)
    
    for (let i = 2; i <= n; i++)
        countArr[i] = countArr[i - 2] + countArr[i - 1]
    
    return countArr[n] % BigInt(1234567)
}