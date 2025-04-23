function solution(n) {
    const countArr = [BigInt(1), BigInt(1)]
    
    for (let i = 2; i <= n; i++)
        countArr.push(countArr[i - 2] + countArr[i - 1])
    
    return countArr[n] % BigInt(1234567)
}