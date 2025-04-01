function solution(picks, minerals) {
    let result = 0
    let [dia, iron, stone] = picks
    let mineralObj = {}
    const mineralObjArray = []
    
    for (let i = 0; i < minerals.length; i++) {
        if (mineralObj[minerals[i]]) mineralObj[minerals[i]]++
        else mineralObj[minerals[i]] = 1
        
        if (((i + 1) % 5 === 0 || i === minerals.length - 1) && mineralObjArray.length < dia + iron + stone) {
            mineralObjArray.push(mineralObj)
            mineralObj = {}
        }
    }
    
    mineralObjArray.sort((a, b) => {
        if ((a.diamond?? 0) === (b.diamond?? 0)) {
            if ((a.iron?? 0) === (b.iron?? 0)) {
                return (b.stone?? 0) - (a.stone?? 0)
            } else return (b.iron?? 0) - (a.iron?? 0)
        } else return (b.diamond?? 0) - (a.diamond?? 0)
    })
    
    for (const obj of mineralObjArray) {
        let pick
        
        if (dia > 0) {
            dia--
            result += (obj.diamond?? 0) + (obj.iron?? 0) + (obj.stone?? 0)
        } else if (iron > 0) {
            iron--
            result += ((obj.diamond?? 0) * 5) + (obj.iron?? 0) + (obj.stone?? 0)
        } else {
            stone--
            result += ((obj.diamond?? 0) * 25) + ((obj.iron?? 0) * 5) + (obj.stone?? 0)
        }
    }
    
    return result
}