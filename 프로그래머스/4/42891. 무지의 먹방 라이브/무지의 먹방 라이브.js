function solution(food_times, k) {
    let index, foodKey
    let sum = 0
    const foodSecObj = {}
    const foodTimeArray = [...food_times]
    
    foodTimeArray.sort((a, b) => a - b)
    
    for (let i = 0; i < foodTimeArray.length; i++) {
        if (i !== 0 && foodTimeArray[i - 1] === foodTimeArray[i]) continue
        
        foodSecObj[foodTimeArray[i]] = foodTimeArray.length - i
    }
    
    const keyArray = Object.keys(foodSecObj).sort((a, b) => a - b)
    
    for (let i = 0; i < keyArray.length; i++) {
        const key = keyArray[i]
        
        if (sum + ((key - (keyArray[i - 1]?? 0)) * foodSecObj[key]) > k) {
            index = ((k - sum) % foodSecObj[key]) + 1
            foodKey = key
            break
        }
        
        sum += (key - (keyArray[i - 1]?? 0)) * foodSecObj[key]
    }
    
    if (!foodKey) return -1
    
    for (let i = 0; i < food_times.length; i++) {
        if (food_times[i] >= foodKey) {
            index--
            
            if (index === 0) return i + 1
        }
    }
}