def findContentChildren(g, s ):
    g.sort(reverse=True)
    s.sort()
    count = 0
    for i in range(len(g)):
        if g[i] >= s[-1]:
            s.pop()
            count += 1
    return count
print(findContentChildren([1,2,3],[1,2]))