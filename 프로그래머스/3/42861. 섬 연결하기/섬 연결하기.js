function solution(n, costs) {    
    costs.sort((a, b) => a[2] - b[2])
    const nodeSet = new Set([costs[0][0], costs[0][1]])
    let result = costs[0][2]
    
    while (nodeSet.size < n) {
        for (const [start, end, cost] of costs) {
            if ((!nodeSet.has(start) && nodeSet.has(end)) || (nodeSet.has(start) && !nodeSet.has(end))) {
                nodeSet.add(start)
                nodeSet.add(end)
                result += cost
                break
            }
        }
    }
    
    return result
}