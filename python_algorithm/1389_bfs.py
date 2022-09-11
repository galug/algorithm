import collections
import sys

def bfs(start):
    visited = [-1] * (len(graph)+1)
    visited[start] = 0
    q= collections.deque([start])
    while q:
        tk = q.popleft()
        for k in graph[tk]:
            if visited[k] == -1:
                visited[k] = visited[tk]+1
                q.append(k)
    return sum(visited)


n, m = map(int,input().split())
graph = collections.defaultdict(list)
min_bfs = [sys.maxsize, 0]
for _ in range(m):
    v, w= map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)
for k in graph:
    graph[k].sort()
for k in sorted(graph.keys()):
    temp = bfs(k)
    if min_bfs[0]>temp:
        min_bfs[0] = temp
        min_bfs[1] = k
print(min_bfs[1])