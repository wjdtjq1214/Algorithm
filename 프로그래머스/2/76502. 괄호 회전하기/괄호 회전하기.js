function solution(s) {
    const strSet = new Set()
    
    for (let i = 0; i < s.length; i++) {
        let flag = true
        const stack = []
        const newStr = s.slice(i) + s.slice(0, i)
        
        for (const char of newStr) {
            if (char === '[' || char === '{' || char === '(') {
                stack.push(char)
            } else {
                if (char === ']') {
                    if (stack[stack.length - 1] === '[') stack.pop()
                    else flag = false
                } else if (char === '}') {
                    if (stack[stack.length - 1] === '{') stack.pop()
                    else flag = false
                } else {
                    if (stack[stack.length - 1] === '(') stack.pop()
                    else flag = false
                }
            }
        }
        
        if (flag && stack.length === 0) strSet.add(newStr)
    }
    
    return strSet.size
}