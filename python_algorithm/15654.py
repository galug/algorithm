import sys

N, M  = map(int,sys.stdin.readline().split())
combi = list(map(int,sys.stdin.readline().split()))
combi.sort()
def dfs(start,result=[]):
    if len(result) == M:
        print(' '.join(map(str,result)))
        return
    for i in range(N):
        if combi[i] not in result:
            dfs(i, result+[combi[i]])
dfs(-1,[])