import sys
sys.setrecursionlimit(10000000)

t = int(input())


def dfs(here, cn, start):
    if visited[here]:
        if here in vt:
            return cn - finished[here]
        return 0
    visited[here] = True
    finished[here] = cn
    vt.add(here)
    return dfs(l[here],cn+1,start)

for _ in range(t):
    n = int(input())
    l = [0] + list(map(int, sys.stdin.readline().split()))
    answer = 0
    finished = [0] * (n + 1)
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        vt = set()
        if visited[i] == False:
            answer += dfs(i, 1, i)
    print(n - answer)
