import sys

def is_oneqt(i,j, n):
    oz = graph[i][j]
    for k in range(i, i+n):
        for l in range(j, j+n):
            if graph[k][l] != oz:
                return False
    return True

def dfs(i, j, n):
    if n==1:
        answer.append(graph[i][j])
        return
    if is_oneqt(i, j, n):
        answer.append(graph[i][j])
        return
    else:
        half = n//2
        answer.append('(')
        dfs(i, j, half)
        dfs(i, j + half, half)
        dfs(i+half, j, half)
        dfs(i + half, j + half, half)
        answer.append(')')

n = int(input())
graph = [sys.stdin.readline() for _ in range(n)]
answer = []
dfs(0,0, n)
print(''.join(answer))