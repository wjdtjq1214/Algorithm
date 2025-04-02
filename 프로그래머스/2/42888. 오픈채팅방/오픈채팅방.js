function solution(record) {
    const userObj = {}
    const messageArray = []
    
    for (const log of record) {
        const [type, userId, nickname] = log.split(' ')
        
        if (type !== 'Leave') userObj[userId] = nickname
        
        if (type !== 'Change') messageArray.push([type, userId])
    }
    
    return messageArray.map(([type, userId]) => `${userObj[userId]}님이 ${type == 'Enter'? '들어왔습니다': '나갔습니다'}.`)
}