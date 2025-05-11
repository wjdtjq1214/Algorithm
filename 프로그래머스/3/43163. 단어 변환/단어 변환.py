from collections import deque

def solution(begin, target, words):
    queue = deque([[begin, 0]])
    wordObj = {}
    visitObj = {
        begin: False
    }
    
    def checkWord(word1, word2):
        differentCount = 0
        
        for i in range(len(word1)):
            if word2[i] != word1[i]:
                differentCount += 1
                
        if differentCount == 1:
            if word2 in wordObj:
                wordObj[word2].append(word1)
            else:
                wordObj[word2] = [word1]
                
            if word1 in wordObj:
                wordObj[word1].append(word2)
            else:
                wordObj[word1] = [word2]

    if words.count(target) == 0:
        return 0
    
    for word in words:
        visitObj[word] = False
        checkWord(word, begin)
                
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            checkWord(words[i], words[j])
    
    while len(queue) > 0:
        [word, count] = queue.popleft()
        visitObj[word] = True
        
        if word in wordObj:
            for nextWord in wordObj[word]:
                if nextWord == target:
                    return count + 1
                
                if not visitObj[nextWord]:
                    queue.append([nextWord, count + 1])
        
    return 0