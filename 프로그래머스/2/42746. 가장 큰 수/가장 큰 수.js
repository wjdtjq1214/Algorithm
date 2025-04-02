function solution(numbers) {
    return BigInt(numbers.sort((a, b) => Number(b + '' + a) - Number(a + '' + b)).join('')).toString()
}