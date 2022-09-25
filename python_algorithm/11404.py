import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[1e9]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    if graph[a][b] > w:
        graph[a][b] = w
for p in range(1,n+1):
    for m in range(1,n+1):
        for n in range(1,n+1):
            if graph[m][n] > graph[m][p] + graph[p][n]:
                graph[m][n] = graph[m][p] + graph[p][n]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(0,end=' ')
            continue
        if graph[i][j] ==1e9:
            print(0, end=' ')
        else:
            print(graph[i][j],end=' ')
    print()