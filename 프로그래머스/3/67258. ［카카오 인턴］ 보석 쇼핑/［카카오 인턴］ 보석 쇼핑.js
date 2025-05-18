function solution(gems) {
    let start = 0, end = 0
    let result = []
    const gemSet = new Set(gems)
    const subGemObj = {}
    const subGemSet = new Set()
    
    while (end < gems.length) {
        if (subGemObj[gems[end]] === undefined) {
            subGemObj[gems[end]] = 1
        } else {
            subGemObj[gems[end]]++
        }
        
        subGemSet.add(gems[end])
        
        if (subGemSet.size === gemSet.size) {
            break
        }
        
        end++
    }
    
    while (start < end) {
        if (subGemObj[gems[start]] === 1) {
            break
        }
        
        subGemObj[gems[start]]--
        start++
    }
    
    result = [start, end]
    
    while (start < gems.length) {
        if (subGemObj[gems[start]] === 1) {
            delete subGemObj[gems[start]]
            subGemSet.delete(gems[start])
        } else {
            subGemObj[gems[start]]--
        }
        
        start++
        
        while (end < gems.length - 1 && gemSet.size !== subGemSet.size) {
            end++
            
            if (subGemObj[gems[end]] === undefined) {
                subGemObj[gems[end]] = 1
            } else {
                subGemObj[gems[end]]++
            }

            subGemSet.add(gems[end])
        }
        
        if (subGemSet.size === gemSet.size && result[1] - result[0] > end - start) {
            result = [start, end]
        }
    }
    
    return [result[0] + 1, result[1] + 1]
}