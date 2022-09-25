import sys
import collections

sys.setrecursionlimit(1000000)

N, M = map(int,sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(M):
    v, w = map(int,sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)
visited = set()
answer = 0
def dfs(v):
    visited.add(v)
    for w in graph[v]:
        if w not in visited:
            dfs(w)
for i in range(1,N+1):
    if i not in graph:
        answer+=1
        continue
    if i not in visited:
        answer+=1
        dfs(i)
print(answer)