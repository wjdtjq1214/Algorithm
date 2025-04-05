function solution(msg) {
    const result = []
    let i = 0, j = 1
    const dic = {
        A: 1,
        B: 2,
        C: 3,
        D: 4,
        E: 5,
        F: 6,
        G: 7,
        H: 8,
        I: 9,
        J: 10,
        K: 11,
        L: 12,
        M: 13,
        N: 14,
        O: 15,
        P: 16,
        Q: 17,
        R: 18,
        S: 19,
        T: 20,
        U: 21,
        V: 22,
        W: 23,
        X: 24,
        Y: 25,
        Z: 26
    }
    
    while (i < msg.length) {
        const str = msg.slice(i, j)
        
        if (dic[str]) {
            if (j == msg.length) {
                result.push(dic[str])
                break
            } else j++
        } else {
            const preStr = str.slice(0, str.length - 1)
            
            dic[str] = Object.keys(dic).length + 1
            
            result.push(dic[preStr])
            
            i += preStr.length
            j = i + 1
        }
    }
    
    return result
}