# 미로 탈출 문제
# 키와 열쇠가 존재
import collections
import sys


# 갈 수 있는 곳인지 판단
def can_go(_y: int, _x: int):
    if 0 <= _y < vertical and 0 <= _x < horizontal and maze[_y][_x] != '#':
        return True
    return False


# key 를 비트로 변환
def convert_key_to_bit(key_bit: int, new_key: str):
    new_key_bit = 1
    new_key_bit <<= (ord(new_key) - 97)
    key_bit |= new_key_bit
    return key_bit


# 대문자 문이 키안에 있는지 탐색하는 함수
def can_open(door: str, keys: int):
    door_bit = 1
    door_bit <<= (ord(door) - 65)
    if door_bit & keys > 0:
        return True
    return False


# 미로 탐색 알고리즘
def bfs():
    # 방문 위치와 que 에 시작 지점과 키의 값 집어넣기
    # 방문 위치는 위치와 키를 모두 포함해서 방문 여부를 판단
    visited = set()
    visited.add((tuple(start), 0))
    que = collections.deque([(start, 0, 0)])
    while que:
        position, key, moving = que.popleft()
        y, x = position[0], position[1]
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 갈 수 없는 곳일 경우 통과
            if not can_go(ny, nx):
                continue
            # key 를 가지고 방문한 적이 없는 경우
            if ((ny, nx), key) not in visited:
                # 탈출구일 경우 탈출
                if maze[ny][nx] == '1':
                    return moving + 1
                # 문이나 열쇠인 경우
                elif maze[ny][nx].isalpha():
                    # 문의 경우
                    if maze[ny][nx].isupper():
                        # 문을 열 수 있는 경우
                        if can_open(maze[ny][nx], key):
                            que.append(([ny, nx], key, moving + 1))
                            visited.add(((ny, nx), key))
                        # 문을 열 수 없는 경우
                        else:
                            continue
                    # 열쇠의 경우
                    else:
                        new_key_bit = convert_key_to_bit(key, maze[ny][nx])
                        que.append(([ny, nx], new_key_bit, moving + 1))
                        visited.add(((ny, nx), new_key_bit))
                # 빈칸이거나 출발지의 경우 이동 가능
                else:
                    que.append(([ny, nx], key, moving + 1))
                    visited.add(((ny, nx), key))
    return -1


# 가로 세로값 입력받기
vertical, horizontal = map(int, sys.stdin.readline().split())
maze = []
start = None
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# maze 입력, 시작 위치
for v in range(vertical):
    line = list(map(str, sys.stdin.readline().rstrip()))
    maze.append(line)
    if '0' in line:
        for h in range(len(line)):
            if line[h] == '0':
                start = [v, h]

print(bfs())
