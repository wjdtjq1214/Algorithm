function solution(park, routes) {
    let point
    
    loop:
    for (let y = 0; y < park.length; y++) {
        for (let x = 0; x < park[y].length; x++) {
            if (park[y][x] == 'S') {
                point = [y, x]
                break loop
            }
        }
    }
    
    for (const route of routes) {
        const [y, x] = point
        const direction = route.split(' ')[0]
        const count = Number(route.split(' ')[1])
        
        if (direction == 'E') {
            const row = park[y]?.split('')
            
            if (x + count < row.length) {
                const directionArray = row?.slice(x, x + count + 1)
                
                if (directionArray?.indexOf('X') == -1) point[1] += count
            }
        } else if (direction == 'W') {
            const row = park[y]?.split('')
            
            if (x - count >= 0) {
                const directionArray = row?.slice(x - count, x + 1)
                
                if (directionArray?.indexOf('X') == -1) point[1] -= count
            }
        } else if (direction == 'S') {
            const col = park.map((row) => row[x])
            
            if (y + count < col.length) {
                const directionArray = col.slice(y, y + count + 1)
                
                if (directionArray?.indexOf('X') == -1) point[0] += count
            }
        } else {
            const col = park.map((row) => row[x])
            
            if (y - count >= 0) {
                const directionArray = col.slice(y - count, y + 1)
                
                if (directionArray?.indexOf('X') == -1) point[0] -= count
            }
        }
    }
    
    return point
}