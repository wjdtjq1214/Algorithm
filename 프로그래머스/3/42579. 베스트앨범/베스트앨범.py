def solution(genres, plays):
    distinctGenresArr = list(set(genres))
    genresPlayCount = [0 for _ in range(len(distinctGenresArr))]
    
    genresDicArr = []
    songDicArr = []
    songIndexArr = []
    
    for i in range(len(genres)):
        genre = genres[i]
        playCount = plays[i]
        
        genresPlayCount[distinctGenresArr.index(genre)] += playCount
        
        songDicArr.append({
            "genre": genre,
            "count": playCount,
            "index": i
        })
        
    for i in range(len(distinctGenresArr)):
        genresDicArr.append({
            "genre": distinctGenresArr[i],
            "count": genresPlayCount[i]
        })
        
    sortGenresDicArr =  sorted(genresDicArr, key = lambda genresDic: genresDic["count"], reverse=True)
        
    for genreObj in sortGenresDicArr:        
        sortedSongArr = sorted(
            list(filter(lambda d: d["genre"] == genreObj["genre"], songDicArr)),
            key = lambda songDic: (-songDic["count"], songDic["index"])
        )
        
        songIndexArr.append(sortedSongArr[0]["index"])
        
        if len(sortedSongArr) != 1:
            songIndexArr.append(sortedSongArr[1]["index"])
            
    return songIndexArr
    