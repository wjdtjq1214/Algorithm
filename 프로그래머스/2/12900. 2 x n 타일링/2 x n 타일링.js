function solution(n) {
    const countArr = new Array(n + 1)
    countArr[0] = 1
    countArr[1] = 1
    
    for (let i = 2; i <= n; i++) {
        countArr[i] = countArr[i - 2] + countArr[i - 1]
        countArr[i] = countArr[i] >= 1000000007? countArr[i] % 1000000007: countArr[i]
    }
    return countArr[n]
}