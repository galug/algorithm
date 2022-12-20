# 파이프 옮기기
# 제한된 이동 범위로만 이동 가능한 파이프를 목적지까지 옮길수 있는 경우의 수
import collections
import sys

n = int(input())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

pipe = [[0, 0], [0, 1]]


def can_move_vertical(y, x) -> bool:
    if y + 1 >= n or graph[y + 1][x] == 1:
        return False
    return True


def can_move_horizontal(y, x) -> bool:
    if x + 1 >= n or graph[y][x + 1] == 1:
        return False
    return True


def can_move_diagonal(y, x) -> bool:
    if y + 1 >= n or x + 1 >= n:
        return False
    if graph[y + 1][x] == 1 or graph[y][x + 1] == 1 or graph[y + 1][x + 1] == 1:
        return False
    return True


def direct_horizontal(temp_pipe):
    start = temp_pipe[0]
    end = temp_pipe[1]
    if start[1] + 1 == end[1]:
        return True
    return False


def direct_vertical(temp_pipe):
    start = temp_pipe[0]
    end = temp_pipe[1]
    if start[0] + 1 == end[0]:
        return True
    return False


def direct_diagonal(temp_pipe):
    if direct_horizontal(temp_pipe) and direct_vertical(temp_pipe):
        return True
    return False


que = collections.deque([pipe])
count = 0
dp = [[0]*n for _ in range(n)]

while que:
    pop_pipe = que.popleft()
    end = pop_pipe[1]
    if end[0] == n - 1 and end[1] == n - 1:
        count += 1
        continue
    if direct_diagonal(pop_pipe):
        if can_move_diagonal(end[0], end[1]):
            que.append([[end[0], end[1]], [end[0] + 1, end[1] + 1]])
        if can_move_vertical(end[0], end[1]):
            que.append([[end[0], end[1]], [end[0] + 1, end[1]]])
        if can_move_horizontal(end[0], end[1]):
            que.append([[end[0], end[1]], [end[0] , end[1]+1]])
    elif direct_vertical(pop_pipe):
        if can_move_diagonal(end[0], end[1]):
            que.append([[end[0], end[1]], [end[0] + 1, end[1] + 1]])
        if can_move_vertical(end[0], end[1]):
            que.append([[end[0], end[1]], [end[0] + 1, end[1]]])
    else:
        if can_move_diagonal(end[0], end[1]):
            que.append([[end[0], end[1]], [end[0] + 1, end[1] + 1]])
        if can_move_horizontal(end[0], end[1]):
            que.append([[end[0], end[1]], [end[0] , end[1]+1]])
print(count)