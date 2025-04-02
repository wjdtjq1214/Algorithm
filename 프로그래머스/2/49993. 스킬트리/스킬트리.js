function solution(skill, skill_trees) {
    var result = 0;
    const skillList = skill.split('')
    
    for (const skillString of skill_trees) {
        const skillIndexList = []
        
        for (const skillChar of skillList) skillIndexList.push(skillString.indexOf(skillChar))
        
        let flag = true
        
        for (let i = 0; i < skillIndexList.length - 1; i++) {
            const thisIndex = skillIndexList[i], nextIndex = skillIndexList[i + 1]
            
            if (thisIndex == -1) {
                if (nextIndex != -1) {
                    flag = false
                    break
                }
            } else if (nextIndex != -1 && thisIndex > nextIndex) {
                flag = false
                break
            }
        }
        
        if (flag) result++
    }
    
    return result;
}