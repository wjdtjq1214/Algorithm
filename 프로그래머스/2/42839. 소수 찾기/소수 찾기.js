function solution(numbers) {
    let result = 0
    const numbersSet = new Set()
    
    function createNum(strNum, numArr) {
        for (let i = 0; i < numArr.length; i++) {
            const newStrNum = strNum + numArr[i]
            numbersSet.add(newStrNum)
            
            createNum(newStrNum, [...numArr.slice(0, i), ...numArr.slice(i + 1)])
        }
    }
    
    createNum('', numbers.split(''))
    
    const countNumObj = getCountNumArr(numbers.length)
    
    for (const num of numbersSet) {
        if (countNumObj[num] === true) {
            result++
        }
    }
    
    return result
}

function getCountNumArr(len) {
    const resultObj = {}
    const numArr = []
    const maxNum = Math.pow(10, len)
    
    for (let i = 0; i <= maxNum; i++)
        numArr.push(i)
    
    for (let i = 2; i <= Math.ceil(Math.sqrt(maxNum)); i++) {
        for (let j = i + i; j <= maxNum; j += i){
            numArr[j] = 0
        }
    }
    
    for (const num of numArr) {
        if (num !== 0 && num !== 1) {
            resultObj[num] = true
        }
    }
    
    return resultObj
}