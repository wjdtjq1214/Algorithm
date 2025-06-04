function solution(babbling) {
    const wordList = ["aya", "ye", "woo", "ma"]
    
    return babbling.filter((sentence) => {
        for (const word of wordList)
            sentence = sentence.split(word).join(' ')
        
        if (sentence == ' '.repeat(sentence.length)) return true
        else return false
    }).length
}