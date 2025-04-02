function solution(players, m, k) {
    let count = 0
    let server = []
    
    for (let i = 0; i < players.length; i++) {
        server = server.filter((obj) => obj.start > i - k)
        
        const serverCount = Math.floor(players[i] / m)
        
        while (server.length < serverCount) {
            server.push({
                start: i
            })
            
            count++
        }
    }
    
    return count
}