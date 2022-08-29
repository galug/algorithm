import collections

dfs_results = []
bfs_results = []
def dfs(v,dic):
    if not dic[v]:
        return
    dfs_results.append(v)
    for nv in dic[v]:
        if nv not in dfs_results:
            dfs(nv, dic)
def bfs(v, dic):
    visited = set([v])
    q = collections.deque([v])
    while q:
        temp_v = q.popleft()
        bfs_results.append(temp_v)
        for nv in dic[temp_v]:
            if nv not in bfs_results and nv not in q:
                q.append(nv)
N, M, V = map(int,input().split())
dict = collections.defaultdict(list)
for _ in range(M):
    v1, v2 = map(int,input().split())
    if v2 not in dict[v1]:
        dict[v1].append(v2)
    if v1 not in dict[v2]:
        dict[v2].append(v1)
for k in dict:
    dict[k].sort()
dfs(V, dict)
bfs(V, dict)
print(' '.join(map(str,dfs_results)))
print(' '.join(map(str,bfs_results)))