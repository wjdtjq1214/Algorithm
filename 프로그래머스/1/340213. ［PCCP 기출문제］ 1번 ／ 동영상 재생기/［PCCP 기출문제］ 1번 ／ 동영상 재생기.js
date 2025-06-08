function solution(video_len, pos, op_start, op_end, commands) {
    let resultTime = ''
    const [maxMin, maxSec] = video_len.split(':').map((str) => Number(str))
    let [min, sec] = pos < op_start || pos > op_end? pos.split(':').map((str) => Number(str)): op_end.split(':').map((str) => Number(str))
    
    for (const command of commands) {
        if (command == 'prev') {
            sec -= 10
            
            if (sec < 0) {
                if (min <= 0) {
                    min = 0
                    sec = 0
                } else {
                    min--
                    sec += 60
                }
            }
        } else {
            sec += 10
            
            if (sec >= 60) {
                min++
                sec = sec - 60
            }
            
            if ((min > maxMin) || (min == maxMin && sec >= maxSec)) {
                min = maxMin
                sec = maxSec
            }
        }
        
        resultTime = ((min >= 10? min: '0' + min) + ':' + (sec >= 10? sec: '0' + sec))
        resultTime = resultTime < op_start || resultTime > op_end? resultTime: op_end
        
        const minSecArray = resultTime.split(':').map((str) => Number(str))
        
        min = minSecArray[0]
        sec = minSecArray[1]
    }    
    
    return resultTime
}