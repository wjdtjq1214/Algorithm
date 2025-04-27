function solution(numbers) {
    const resultArray = new Array(numbers.length)
    const preArray = []
    
    for (let i = 0; i < numbers.length; i++) {        
        for (let j = preArray.length - 1; j >= 0 && preArray[j].number < numbers[i]; j--) {
            resultArray[preArray.pop().index] = numbers[i]
        }
        
        preArray.push({
            index: i,
            number: numbers[i]
        })
    }
    
    for (const obj of preArray) {
        resultArray[obj.index] = -1
    }
    
    return resultArray
}