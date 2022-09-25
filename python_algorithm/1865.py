import collections
import sys

tc = int(input())
answer = []
for _ in range(tc):
    n, m, w = map(int,sys.stdin.readline().split())
    edges = []
    inf_cycle = True
    dist = [500000]*(n+1)
    dist[1] = 0
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(w):
        s, e, t =map(int,sys.stdin.readline().split())
        edges.append([s,e,t*-1])
    for i in range(n):
        for s,e,t in edges:
            if dist[e] > dist[s] + t:
                if i == n-1:
                    inf_cycle=False
                    break
                dist[e] = dist[s] +t
    if inf_cycle ==False:
        answer.append('YES')
    else:
        answer.append('NO')
for ele in answer:
    print(ele)