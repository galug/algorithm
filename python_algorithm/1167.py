import collections
import sys
sys.setrecursionlimit(1000000)

n = int(input())
graph = collections.defaultdict(list)
for i in range(1,n+1):
    l = list(map(int,sys.stdin.readline().split()))
    vertex = l[0]
    for j in range(1, len(l)-1,2):
        graph[vertex].append([l[j],l[j+1]])
visited = [-1]*(n+1)
def dfs(v):
    for nv, nd in graph[v]:
        if visited[nv] ==-1:
            visited[nv] = visited[v] + nd
            dfs(nv)
visited[1] = 0
dfs(1)
nv = visited.index(max(visited))
visited = [-1]*(n+1)
visited[nv] = 0
dfs(nv)
print(max(visited))