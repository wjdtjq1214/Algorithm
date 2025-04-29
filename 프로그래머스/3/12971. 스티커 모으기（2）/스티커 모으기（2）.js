function solution(sticker) {
    const scoreLength = sticker.length
    const notContain0SumScoreArr = new Array(scoreLength)
    const contain0SumScoreArr = new Array(scoreLength)
    
    if (sticker.length < 4) {
        return Math.max(...sticker)
    }
    
    notContain0SumScoreArr[0] = 0
    notContain0SumScoreArr[1] = sticker[1]
    contain0SumScoreArr[0] = sticker[0]
    contain0SumScoreArr[1] = 0
    
    for (let i = 2; i < scoreLength; i++) {
        const thisScore = sticker[i]
        let notContain0Sum, contain0Sum
        
        if (i > 2) {
            notContain0Sum = Math.max(notContain0SumScoreArr[i - 3], notContain0SumScoreArr[i - 2]) + thisScore
            contain0Sum = Math.max(contain0SumScoreArr[i - 3], contain0SumScoreArr[i - 2]) + thisScore
        } else {
            notContain0Sum = notContain0SumScoreArr[i - 2] + thisScore
            contain0Sum = contain0SumScoreArr[i - 2] + thisScore
        }
        
        notContain0SumScoreArr[i] = notContain0Sum
        contain0SumScoreArr[i] = i === scoreLength - 1? 0: contain0Sum
    }
    
    return Math.max(notContain0SumScoreArr[scoreLength - 3], notContain0SumScoreArr[scoreLength - 2], notContain0SumScoreArr[scoreLength - 1], contain0SumScoreArr[scoreLength - 3], contain0SumScoreArr[scoreLength - 2], contain0SumScoreArr[scoreLength - 1])
}