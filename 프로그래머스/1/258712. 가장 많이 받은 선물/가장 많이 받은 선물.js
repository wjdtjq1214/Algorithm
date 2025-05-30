function solution(friends, gifts) {
    const giftCountArray = []
    const giftScore = {}
    const giftObj = {}
    
    for (gift of gifts) {
        if (giftObj[gift]) giftObj[gift]++
        else giftObj[gift] = 1
        
        const [sender, receiver] = gift.split(' ')
        
        if (giftScore[sender]) giftScore[sender]++
        else giftScore[sender] = 1
        
        if (giftScore[receiver]) giftScore[receiver]--
        else giftScore[receiver] = -1
    }
    
    for (let i = 0; i < friends.length; i++) {
        let count = 0
        const sender = friends[i]
        
        for (let j = 0; j < friends.length; j++) {
            if (i == j) continue
            
            const receiver = friends[j]
            const sendCount = giftObj[sender + ' ' + receiver]?? 0
            const receiveCount = giftObj[receiver + ' ' + sender]?? 0
            
            if (sendCount > receiveCount || (sendCount == receiveCount && (giftScore[sender]?? 0) > (giftScore[receiver]?? 0))) count++
        }
        
        giftCountArray.push(count)
    }
    
    return Math.max(...giftCountArray)
}