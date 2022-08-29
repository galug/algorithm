import collections

N = int(input())
dyn = {0:0, 1:0}
def dfs(n):
    if n in dyn:
        return dyn[n]
    dyn[n] = min(dfs(n-1),dfs(n//2)+n%2,dfs(n//3)+n%3)+1
    return dyn[n]
print(dfs(N))