import collections
import heapq
import sys

vn,en =map(int,sys.stdin.readline().split())
start = int(input())
graph = graph = [[] for _ in range(vn + 1)]
for _ in range(en):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])
dist = [float('inf')]*(vn+1)
dist[start] = 0
heap = [(0,start)]
while heap:
    d, v = heapq.heappop(heap)
    if dist[v] < d:
        continue
    for nv, nd in graph[v]:
        temp =nd +d
        if temp < dist[nv]:
            heapq.heappush(heap,(temp,nv))
            dist[nv] = temp
for i in range(1, len(dist)):
    if dist[i] != float('inf'):
        print(dist[i])
    else:
        print('INF')
