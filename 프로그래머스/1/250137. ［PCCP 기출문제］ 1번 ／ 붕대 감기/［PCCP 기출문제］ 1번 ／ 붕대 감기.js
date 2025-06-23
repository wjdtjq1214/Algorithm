function solution(bandage, health, attacks) {
    let nowHealth = health
    
    for (let i = 0; i < attacks.length; i++) {
        if (i != 0) {
            const continueSec = attacks[i][0] - attacks[i - 1][0] - 1
            
            const heal = (Math.floor(continueSec / bandage[0]) * bandage[2]) + (continueSec * bandage[1])
            
            nowHealth = nowHealth + heal >= health? health: nowHealth + heal
        }
        
        nowHealth -= attacks[i][1]
        
        if (nowHealth <= 0) return -1
    }
    
    return nowHealth
}