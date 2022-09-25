import collections
import sys

sys.setrecursionlimit(1000000)
n = int(input())
graph = collections.defaultdict(list)
for _ in range(n-1):
    parent, children, weight = map(int,sys.stdin.readline().split())
    graph[parent].append((children,weight))
    graph[children].append((parent, weight))

def dfs(v):
    for child, w in graph[v]:
        if visited[child] == -1:
            visited[child] = visited[v] + w
            dfs(child)

visited = [-1]*(n+1)
visited[1] = 0
dfs(1)
nv = visited.index(max(visited))
visited = [-1]*(n+1)
visited[nv] = 0
dfs(nv)
print(max(visited))