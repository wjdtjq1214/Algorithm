function solution(toppings) {
    let result = 0
    const totalObj = {}
    const divideObj = {}
    const totalSet = new Set()
    const divideSet = new Set()
    
    for (const topping of toppings) {
        if (totalObj[topping]) totalObj[topping]++
        else {
            totalObj[topping] = 1
            totalSet.add(topping)
        }
    }
    
    for (const topping of toppings) {
        if (divideObj[topping]) divideObj[topping]++
        else {
            divideObj[topping] = 1
            divideSet.add(topping)
        }
        
        totalObj[topping]--
        
        if (totalObj[topping] === 0) {
            delete totalObj[topping]
            totalSet.delete(topping)
        }
        
        if (divideSet.size === totalSet.size) result++
    }
    
    return result
}