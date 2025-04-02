function solution(book_time) {
    let maxLength = 0
    let roomArray = []
    
    book_time.sort((a, b) => a[0] > b[0]? 1: -1)
    
    for (const book of book_time) {
        roomArray = roomArray.filter(([start, end]) => end > book[0])
        
        let [endHour, endMin] = book[1].split(':')
        
        if (Number(endMin) + 10 > 60) {
            endMin = (Number(endMin) - 50 < 10? '0': '') + (Number(endMin) - 50).toString()
            endHour = (Number(endHour) + 1 < 10? '0': '') + (Number(endHour) + 1).toString()
        } else {
            endMin = (Number(endMin) + 10).toString()
        }
        
        book[1] = endHour + ':' + endMin
        roomArray.push(book)
        maxLength = maxLength < roomArray.length? roomArray.length: maxLength
    }
    
    return maxLength
}