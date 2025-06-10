function solution(id_list, report, k) {
    const banObj = {}
    const idListCountObj = {}
    
    for (const banStr of report) {
        const [id, banId] = banStr.split(' ')
        
        if (banObj[banId]) {            
            if (banObj[banId].indexOf(id) == -1) banObj[banId].push(id)
        } else banObj[banId] = [id]
    }
    
    for (const banId in banObj) {
        if (banObj[banId].length >= k) {
            for (const id of banObj[banId]) {
                if (idListCountObj[id]) {
                    idListCountObj[id]++
                } else idListCountObj[id] = 1
            }
        }
    }
    
    return id_list.map((id) => {
        return idListCountObj[id]? idListCountObj[id]: 0
    })
}