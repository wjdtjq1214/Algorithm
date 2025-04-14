function solution(s) {
    const result = []
    const tupleArray = s.slice(2, s.length - 2).split('},{').map((str) => str.split(',')).sort((a, b) => a.length - b.length)
    
    for (let i = 0; i < tupleArray.length; i++) {
        if (i == 0) result.push(Number(tupleArray[i][0]))
        else {
            for (const num of tupleArray[i])
                if (result.indexOf(Number(num)) == -1)
                    result.push(Number(num))
        }
    }
    
    return result
}