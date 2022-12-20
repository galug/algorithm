# 미로탐색
# N x M 크기의 미로에서 목적지에 갈 수 있는 최소 거리
import collections
import sys

#
vertical, horizontal = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(vertical)]
visited = [[0] * horizontal for _ in range(vertical)]


def can_move(y, x):
    if 0 <= y < vertical and 0 <= x < horizontal and graph[y][x] == 1:
        return True
    return False


direct_x = [1, -1, 0, 0]
direct_y = [0, 0, 1, -1]
sum(direct_x)
def bfs():
    que = collections.deque([[0, 0]])
    count = 0
    while que:
        len_que = len(que)
        count += 1
        for _ in range(len_que):
            y, x = que.popleft()
            if y == vertical - 1 and x == horizontal - 1:
                return count
            for i in range(4):
                move_y, move_x = direct_y[i], direct_x[i]
                if can_move(y + move_y, x + move_x):
                    que.append([y + move_y, x + move_x])
                    graph[y + move_y][x + move_x] = 0


print(bfs())
