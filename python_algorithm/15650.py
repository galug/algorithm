import sys

N, M = map(int,sys.stdin.readline().split())
def dfs(j,result=[]):
    if len(result) == M:
        print(' '.join(map(str,result)))
        return
    for i in range(j,N+1):
        result.append(i)
        dfs(i+1, result)
        result.pop()
dfs(1,[])