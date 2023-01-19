# 백조의 호수
# 그래프를 계속하여 갱신하면서 만날 수 있는지 판단
import collections
import sys


# 호수 그리는 함수
def draw_lake():
    print('====================================')
    for _y in range(vertical):
        for _x in range(horizontal):
            print(visited[_y][_x], end='')
        print()


# 얼음을 녹이는 함수
def melt():
    global number_of_water
    next_waters = set()
    # draw_lake()
    for nma in next_melted_area:
        for nma_y, nma_x in next_melted_area[nma]:
            if visited[nma_y][nma_x] != -1:

                continue
            visited[nma_y][nma_x] = nma
            next_waters += 1


# 벽인지 판단하는 함수
def is_wall(y: int, x: int):
    if y < 0 or y >= vertical or x < 0 or x >= horizontal:
        return True
    return False


# 갈 수 있는 곳인지 판단하는 함수
def can_go(y: int, x: int):
    if visited[y][x] == -1 and (lake[y][x] == '.' or lake[y][x] == 'L'):
        return True
    return False


# area 를 만드는 함수
def make_area(_y: int, _x: int, wn: int):
    global melted_area_number
    que = collections.deque([(_y, _x)])
    new_area = set()
    visited[_y][_x] = wn
    new_area.add((_y, _x))
    new_melted_area = set()
    while que:
        wy, wx = que.popleft()
        melted_area_number += 1
        for dy, dx in direction:
            nwy, nwx = wy + dy, wx + dx
            if is_wall(nwy, nwx):
                continue
            if lake[nwy][nwx] == '.' or lake[nwy][nwx] == 'L':
                if visited[nwy][nwx] == -1:
                    que.append((nwy, nwx))
                    new_area.add((nwy, nwx))
                    visited[nwy][nwx] = wn
            else:
                new_melted_area.add((nwy, nwx))
    waters[wn] = new_area
    next_melted_area[wn] = new_melted_area


vertical, horizontal = map(int, sys.stdin.readline().split())

lake = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(vertical)]
swan = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
waters = {}
waters_number = 0
next_melted_area = {}
melted_area_number = 0
visited = [[-1] * horizontal for _ in range(vertical)]

for i in range(vertical):
    for j in range(horizontal):
        if visited[i][j] != -1 or lake[i][j] == 'X':
            continue
        make_area(i, j, waters_number)
        waters_number += 1
print(next_melted_area)
while melted_area_number != horizontal * vertical:
    melt()
    break
