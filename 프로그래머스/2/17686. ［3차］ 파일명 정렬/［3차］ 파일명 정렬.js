function solution(files) {
    const fileInfoArray = files.map((name, index) => {
        const numberStartIndex = name.match(/\d/).index
        const numberString = name.slice(numberStartIndex, name.length)
        const numberEndIndex = numberString.match(/\D/)?.index?? numberString.length
        const head = (name.slice(0, numberStartIndex)?? '').toLowerCase()
        const number = Number(numberString.slice(0, numberEndIndex))
        
        return {head, number, name, index}
    })
    
    return fileInfoArray.sort((a, b) => {
        if (a.head > b.head) return 1
        else if (a.head < b.head) return -1
        else {
            if (a.number == b.number) return a.index - b.index
            else return a.number - b.number
        }
    }).map((fileObj) => fileObj.name)
}