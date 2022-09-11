import collections
import sys

N, M = map(int,sys.stdin.readline().split())
graph = [[sys.maxsize]*(N+1) for i in range(N+1)]
for i in range(N+1):
    graph[i][i] = 0
    graph[i][0] = 0
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    graph[v][w] = 1
    graph[w][v] = 1
for p in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if graph[i][p] + graph[p][j] <graph[i][j]:
                graph[i][j] = graph[i][p] +graph[p][j]
answer = [sys.maxsize,-1]
for i in range(1,N+1):
    if answer[0] > sum(graph[i]):
        answer[0] = sum(graph[i])
        answer[1] = i
print(answer[1])