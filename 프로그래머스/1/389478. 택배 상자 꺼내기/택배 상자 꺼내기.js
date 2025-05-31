function solution(n, w, num) {
    const count = Math.floor((n - num) / (w * 2)) * 2
    const last = (n - num) % (w * 2)
    const numLastCount = num % w
    
    let plus = (numLastCount === 0 && last >= 1) || (numLastCount !== 0 && last >= (w - numLastCount) * 2 + 1)? 1: 0
    
    return 1 + count + plus
}