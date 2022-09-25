import collections
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    dq = collections.deque()
    dq.append([0, 0, 0])
    visited[0][0][0] = 1
    while dq:
        y, x, crash = dq.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x][crash]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if graph[ny][nx] == 0 and visited[ny][nx][crash] == 0:
                dq.append([ny, nx, crash])
                visited[ny][nx][crash] = visited[y][x][crash]+1
            if graph[ny][nx] == 1 and crash == 0:
                visited[ny][nx][crash+1] = visited[y][x][crash]+1
                dq.append([ny,nx,crash+1])
    return -1
print(bfs())
