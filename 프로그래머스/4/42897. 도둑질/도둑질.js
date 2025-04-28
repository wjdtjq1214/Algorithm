function solution(money) {
    const moneyLength = money.length
    const notContain0SumMoneyArr = new Array(moneyLength)
    const contain0SumMoneyArr = new Array(moneyLength)
    notContain0SumMoneyArr[0] = 0
    notContain0SumMoneyArr[1] = money[1]
    contain0SumMoneyArr[0] = money[0]
    contain0SumMoneyArr[1] = 0
    
    for (let i = 2; i < moneyLength; i++) {
        const thisMoney = money[i]
        let notContain0Sum, contain0Sum
        
        if (i > 2) {
            notContain0Sum = Math.max(notContain0SumMoneyArr[i - 3], notContain0SumMoneyArr[i - 2]) + thisMoney
            contain0Sum = Math.max(contain0SumMoneyArr[i - 3], contain0SumMoneyArr[i - 2]) + thisMoney
        } else {
            notContain0Sum = notContain0SumMoneyArr[i - 2] + thisMoney
            contain0Sum = contain0SumMoneyArr[i - 2] + thisMoney
        }
        
        notContain0SumMoneyArr[i] = notContain0Sum
        contain0SumMoneyArr[i] = i === moneyLength - 1? 0: contain0Sum
    }
    
    return Math.max(notContain0SumMoneyArr[moneyLength - 3], notContain0SumMoneyArr[moneyLength - 2], notContain0SumMoneyArr[moneyLength - 1], contain0SumMoneyArr[moneyLength - 3], contain0SumMoneyArr[moneyLength - 2], contain0SumMoneyArr[moneyLength - 1])
}