import collections
import sys

t= int(input())

def unlock():
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j].isupper():
                if graph[i][j].lower() in keys:
                    graph[i][j] = '.'
    keys.clear()
def bfs():
    visited = [[0]*(w+2) for _ in range(h+2)]
    q = collections.deque([[0,0]])
    pyx = [[0,1],[0,-1],[1,0],[-1,0]]
    a = 0
    while q:
        y,x = q.popleft()
        for py,px in pyx:
            ty, tx = y + py, x+px
            if tx<0 or tx >= w+2 or ty<0 or ty >= h+2 or visited[ty][tx] == 1:
                continue
            if graph[ty][tx] == '*' or graph[ty][tx].isupper():
                continue
            if graph[ty][tx].islower():
                keys.append(graph[ty][tx])
                graph[ty][tx] = '.'
            if graph[ty][tx] == '$':
                a += 1
                graph[ty][tx] = '.'
            visited[ty][tx] = 1
            q.append([ty,tx])
    return a
for _ in range(t):
    h, w = map(int,sys.stdin.readline().split())
    graph = []
    q = collections.deque()
    answer = 0
    for i in range(h+2):
        if i == 0 or i==h+1:
            graph.append(['.']*(w+2))
        else:
            graph.append(['.'] + list(map(str, sys.stdin.readline().rstrip()))+['.'])
    keys = list(map(str,sys.stdin.readline().rstrip()))
    if keys[0] == '0':
        keys.pop(0)
    answer += bfs()
    while keys:
        unlock()
        answer += bfs()
    answer += bfs()

    print(answer)