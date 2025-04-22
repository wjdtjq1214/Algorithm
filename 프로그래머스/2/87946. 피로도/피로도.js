function solution(k, dungeons) {
    let maxCount = 0
    
    dungeons = dungeons.filter(([needValue, minusValue]) => needValue <= k)
    
    if (dungeons.length === 0) return maxCount
    
    for (let i = 0; i < dungeons.length; i++){
        loop(k - dungeons[i][1], [...dungeons.slice(0, i), ...dungeons.slice(i + 1, dungeons.length)], 1)
    }
    
    function loop(remainValue, dungeonArr, count) {
        dungeonArr = dungeonArr.filter(([needValue, minusValue]) => needValue <= remainValue)
        
        if (dungeonArr.length == 0) {
            maxCount = maxCount > count? maxCount: count
        } else {
            for (let i = 0; i < dungeonArr.length; i++) {
                loop(remainValue - dungeonArr[i][1], [...dungeonArr.slice(0, i), ...dungeonArr.slice(i + 1, dungeonArr.length)], count + 1)
            }
        }
    }
    
    return maxCount
}