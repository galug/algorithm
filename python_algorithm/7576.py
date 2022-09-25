from collections import deque
import sys


def bfs():
    m, n = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    tmt_cnt = 0
    tmt = deque()

    day = 0

    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 0):
                tmt_cnt += 1
            elif(graph[i][j] == 1):
                tmt.append((i, j))

    # days 에 익은 토마토들 다 큐에서 빼내버리기
    while tmt and tmt_cnt:
        for _ in range(len(tmt)):
            x, y = tmt.popleft()

            if x > 0 and graph[x - 1][y] == 0:
                graph[x - 1][y] = 1
                tmt.append((x - 1, y))
                tmt_cnt -= 1
            if x < n - 1 and graph[x + 1][y] == 0:
                graph[x + 1][y] = 1
                tmt.append((x + 1, y))
                tmt_cnt -= 1
            if y > 0 and graph[x][y - 1] == 0:
                graph[x][y - 1] = 1
                tmt.append((x, y - 1))
                tmt_cnt -= 1
            if y < m - 1 and graph[x][y + 1] == 0:
                graph[x][y + 1] = 1
                tmt.append((x, y + 1))
                tmt_cnt -= 1
        day += 1

    if tmt_cnt:
        print(-1)
    else:
        print(day)


if __name__ == '__main__':
    bfs()