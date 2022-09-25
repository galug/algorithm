import sys

tc = int(input())
answer = []

def bellman_ford(n:int,edges):
    dist = [500000] * (n + 1)
    dist[1] = 0
    for i in range(n-1):
        inf_cycle = True
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                inf_cycle = False
        if inf_cycle:
            return False

    for s, e, t in edges:
        if dist[e] > dist[s]+t:
            return True
    return False
for _ in range(tc):
    n, m, w = map(int,sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(w):
        s, e, t =map(int,sys.stdin.readline().split())
        edges.append([s,e,t*-1])
    if bellman_ford(n,edges):
        print('YES')
    else:
        print('NO')