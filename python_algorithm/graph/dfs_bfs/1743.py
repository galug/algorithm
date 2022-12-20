# bfs 로 최대 영역 구하는 문제
import collections
import sys

vertical, horizontal, number_of_trash = map(int, sys.stdin.readline().split())
graph = [[0] * horizontal for _ in range(vertical)]
for _ in range(number_of_trash):
    r, c = map(int, sys.stdin.readline().split())
    graph[r-1][c-1] = '#'

direct_y = [0, 0, -1, 1]
direct_x = [1, -1, 0, 0]

# bfs 를 사용한다.
def bfs(y: int, x: int) -> int:
    que = collections.deque([[y, x]])
    graph[y][x] = '.'
    count_trash = 1
    # 최대 영역을 구하기 위해 que 를 이용한다.
    while que:
        y, x = que.popleft()
        # 4 방향을 모두 확인한다.
        for move_index in range(4):
            move_y = direct_y[move_index]
            move_x = direct_x[move_index]
            # 쓰레기에 속한다면 4방향으로 확인하고 que에 추가한다.
            if is_trash(y + move_y, x + move_x):
                count_trash += 1
                graph[y+move_y][x+move_x] = '.'
                que.append([y + move_y, x + move_x])
    return count_trash

def is_trash(y, x):
    if 0 <= y < vertical and 0 <= x < horizontal and graph[y][x] == '#':
        return True
    return False


answer = 0

for i in range(vertical):
    for j in range(horizontal):
        if is_trash(i, j):
            count = bfs(i, j)
            answer = max(answer, count)

print(answer)
