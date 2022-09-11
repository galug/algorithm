import collections
import sys

def dfs(v, visited:list, graph:dict):
    visited.append(v)
    for w in sorted(graph[v]):
        if w not in visited:
            dfs(w,visited,graph)
    return visited

def bfs(v, graph:dict):
    visited = [v]
    que = collections.deque([v])
    while que:
        node = que.popleft()
        for w in sorted(graph[node]):
            if w not in visited:
                visited.append(w)
                que.append(w)
    return visited
N, M , V = map(int,sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(M):
    v, w = map(int,sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)

print(' '.join(str(n) for n in dfs(V,[],graph)))
print(' '.join(str(n) for n in bfs(V,graph)))