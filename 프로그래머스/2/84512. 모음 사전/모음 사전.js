function solution(word) {
    const wordArr = []
    let count = 0
    const words = ['A', 'E', 'I', 'O', 'U']
    let result = 0
    
    for (const char of words)
        loop(char)
    
    function loop(wordString) {
        wordArr.push(wordString)
        if (wordString.length < 5) {
            count++
        
            for (const char of words) {
                const newWord = wordString + char

                loop(newWord)
            }
        }
    }
    
    return wordArr.indexOf(word) + 1
}