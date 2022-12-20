# 그래프에서의 모든 곳곳에서 상어까지의 최대 거리를 찾는다.
import sys

vertical, horizontal = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(vertical)]
answer = 0



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