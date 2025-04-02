function solution(fees, records) {
    const [baseMin, baseFee, standardMin, fee] = fees
    const recordObj = {}
    
    for (const record of records) {
        const [time, car, type] = record.split(' ')
        
        if (recordObj[car]) recordObj[car].push(`${time} ${type}`)
        else recordObj[car] = [`${time} ${type}`]
    }
    
    return Object.keys(recordObj).sort().map((car) => {
        let totalMin = 0
        
        const carRecords = recordObj[car]
        
        for (let i = 0; i < carRecords.length; i = i + 2) {
            if (carRecords[i + 1]) {
                const [inHour, inMin] = carRecords[i].slice(0, 5).split(':')
                const [outHour, outMin] = carRecords[i + 1].slice(0, 5).split(':')
                
                totalMin += ((Number(outHour) - Number(inHour)) * 60) + (Number(outMin) - Number(inMin))
            } else {
                const [inHour, inMin] = carRecords[i].slice(0, 5).split(':')
                
                totalMin += ((23 - Number(inHour)) * 60) + (59 - Number(inMin))
            }
        }
        
        return baseFee + (Math.ceil((totalMin - baseMin > 0? totalMin - baseMin: 0) / standardMin) * fee)
    })
}