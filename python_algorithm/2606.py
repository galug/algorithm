import collections
import sys

vn = int(input())
en = int(input())

def dfs(v:int):
    visited.add(v)
    for w in graph[v]:
        if w not in visited:
            dfs(w)

graph = collections.defaultdict(list)
visited = set()
for _ in range(en):
    v, w = map(int,sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)
dfs(1)
print(len(visited)-1)