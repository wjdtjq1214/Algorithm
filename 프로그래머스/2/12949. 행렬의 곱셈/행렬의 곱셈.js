function solution(arr1, arr2) {
    const changedArr2 = Array.from(Array(arr2[0].length), () => new Array(arr2.length))
    const result = []
    
    for (let i = 0; i < arr2.length; i++) {
        for (let j = 0; j < arr2[i].length; j++) {
            changedArr2[j][i] = arr2[i][j]
        }
    }
    
    for (let i = 0; i < arr1.length; i++) {
        const sumArray = []
        
        for (const arr2Row of changedArr2) {
            let sum = 0
            
            for (let index = 0; index < arr2Row.length; index++) {
                sum += arr1[i][index] * arr2Row[index]
            }
            
            sumArray.push(sum)
        }
            
        result.push(sumArray)
    }
    
    return result
}