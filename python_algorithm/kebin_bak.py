import collections
import sys

N, M = map(int,input().split())
graph = collections.defaultdict(list)
min_bak = sys.maxsize
answer = 0
def bfs(v, d):
    visited = [-1] * (N+1)
    visited[v] = 0
    q = collections.deque([v])
    while q:
        cv = q.popleft()
        for nv in d[cv]:
            if visited[nv] == -1:
                q.append(nv)
                visited[nv] = visited[cv] + 1
    return sum(visited) + 1
for _ in range(M):
    v1, v2 = map(int,input().split())
    if v2 not in graph[v1]:
        graph[v1].append(v2)
    if v1 not in graph[v2]:
        graph[v2].append(v1)
for k in sorted(graph.keys()):
    b_a = bfs(k, graph)
    if min_bak > b_a:
        min_bak = b_a
        answer = k
print(answer)