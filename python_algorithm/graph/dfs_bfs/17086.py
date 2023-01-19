# 그래프에서의 모든 곳곳에서 상어까지의 최대 거리를 찾는다.
import collections
import sys

vertical, horizontal = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(vertical)]
answer = 0
que = collections.deque()
move = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

# 상어가 있는 칸을 큐에 추가
for i in range(vertical):
    for j in range(horizontal):
        if graph[i][j] == 1:
            que.append((i, j))

while que:
    # 이동한 위치
    y, x = que.popleft()
    # 이동할 위치의 벡터를 뽑아낸다.
    for move_y, move_x in move:
        new_y = y + move_y
        new_x = x + move_x
        # 이동이 불가능 할 시 넘어간다.
        if new_x >= horizontal or new_x < 0 or new_y >= vertical or new_y < 0 or graph[new_y][new_x] > 0:
            continue
        # graph[new_y][new_x] == 0 일때 que 에 추가하고 이전 위치 + 1 을 해준다.
        graph[new_y][new_x] = graph[y][x] + 1
        que.append((new_y, new_x))
        answer = max(answer, graph[y][x] + 1)

print(answer - 1)

'''
나의 최초 풀이 
느린 브루트 포스식 풀이 

## 상어가 있는 지 확인 
def is_shark(y: int, x: int) -> bool:
    if 0 <= y < vertical and 0 <= x < horizontal and graph[y][x] == 1:
        return True
    return False

## 상어가 나오는 데 까지 걸린 거리 
def get_distance(y: int, x: int):
    dist = 1
    while True:
        for move in range(-1 * dist, dist + 1):
            if is_shark(y + dist, x + move):
                return dist
            if is_shark(y - dist, x + move):
                return dist
            if is_shark(y + move, x + dist):
                return dist
            if is_shark(y + move, x - dist):
                return dist
        dist += 1

## 모든 좌표에서 상어까지의 거리를 확인해 준다. 
for i in range(vertical):
    for j in range(horizontal):
        if graph[i][j] == 0:
            distance = get_distance(i, j)
            answer = max(answer, distance)

print(answer)
'''
