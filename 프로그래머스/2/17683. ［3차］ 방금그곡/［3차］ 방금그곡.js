function solution(m, musicinfos) {
    let resultArr = [];
    const changeObj = {
        'C#': 'H',
        'D#': 'I',
        'F#': 'J',
        'G#': 'K',
        'A#': 'L',
        'B#': 'M'
    }
    
    for (const key in changeObj)
        m = m.split(key).join(changeObj[key])
    
    for (let i = 0; i < musicinfos.length; i++) {
        const musicinfo = musicinfos[i]
        let totalMusic = ''
        let [start, end, name, music] = musicinfo.split(',')
        const [startHour, startMin] = start.split(':')
        const [endHour, endMin] = end.split(':')
        
        const time = (Number(endHour) - Number(startHour)) * 60 + Number(endMin) - Number(startMin)
        
        for (const key in changeObj)
            music = music.split(key).join(changeObj[key])
        
        for (let i = 0; i < time; i++)
            totalMusic += music[i % music.length]
        
        if (totalMusic.indexOf(m) !== -1)
            resultArr.push([name, time, i])
    }
    
    if (resultArr.length === 0)
        return '(None)'
    
    resultArr.sort((a, b) => {
        if (a[1] === b[1]) {
            return a[2] - b[2]
        } else
            return b[1] - a[1]
    })
    
    return resultArr[0][0]
}