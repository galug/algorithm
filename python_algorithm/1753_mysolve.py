import collections
import heapq
import sys

vn,en =map(int,sys.stdin.readline().split())
start = int(input())
graph = collections.defaultdict(list)
for _ in range(en):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])
dist = [-1]*(vn+1)
heap = []
heapq.heappush(heap,[0,start])
while heap:
    hp = heapq.heappop(heap)
    if dist[hp[1]] != -1:
        continue
    dist[hp[1]] = hp[0]
    for v,d in graph[hp[1]]:
        if dist[v] == -1:
            heapq.heappush(heap,[hp[0]+d,v])
for i in range(1,len(dist)):
    if dist[i] == -1:
        print('INF')
        continue
    print(dist[i])