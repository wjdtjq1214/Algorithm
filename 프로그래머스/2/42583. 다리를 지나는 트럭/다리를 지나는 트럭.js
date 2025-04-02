function solution(bridge_length, weight, truck_weights) {
    let time = 1
    let sum = 0
    let nowTruckArray = []
    
    for (let i = 0; i < truck_weights.length; i++) {
        let newSum = 0
        const newTruckArray = []
        
        for (const obj of nowTruckArray) {
            if (obj.end > time) {
                newTruckArray.push(obj)
                newSum += obj.weight
            }
        }
        
        sum = newSum
        nowTruckArray = newTruckArray
            
        const truckWeight = truck_weights[i]
        
        if (nowTruckArray.length === 0) {
            sum += truckWeight
            nowTruckArray.push({
                weight: truckWeight,
                end: time + bridge_length
            })
            
            time++
            
            continue
        }
        
        while (sum + truckWeight > weight) {
            sum -= nowTruckArray[0].weight
            time = nowTruckArray[0].end
            nowTruckArray = nowTruckArray.slice(1)
        }
                
        if (bridge_length < nowTruckArray.length + 1) {
            sum -= nowTruckArray[0].weight
            time = nowTruckArray[0].end
            nowTruckArray = nowTruckArray.slice(1)
        }
        
        nowTruckArray.push({
            weight: truckWeight,
            end: time + bridge_length
        })
        
        time++
        sum += truckWeight
    }
    
    return nowTruckArray[nowTruckArray.length - 1].end
}