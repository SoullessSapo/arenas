def bicoloring(graph,colors, c, n):
    if colors[pos] != -1 and colors[pos] != c:
        colors[pos] = c
    res = True
    for i in range(n):
        if graph[i]:
            if colors[pos][i] == -1:
                res &= bicoloring(graph,colors,i,1-c,n)
            if colors[i] != -1 and colors[i] != 1-c:
                return False
        if not res:
            return False
        return True
