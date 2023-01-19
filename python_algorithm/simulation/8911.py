# 거북이의 이동 최대 반경을 구하라
import sys


def move():
    pass

# 테스트 케이스의 수
tc = int(input())
# direction(y,x)
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(tc):
    # 이동한 루트를 입력받음
    route = list(map(str, sys.stdin.readline().rstrip()))
    # 북쪽을 향하고 0,0 에 위치하게끔 세팅
    d = 0
    y, x = 0, 0
    # 거북이가 이동했던 최대값과 최소값을 통해서 거북이의 이동 범위를 구할 수 있다.
    max_y, max_x, min_y, min_x = 0, 0, 0, 0
    for r in route:
        # 거북이의 이동 방향 설정
        dy, dx = direction[d]
        # 앞으로 이동
        if r == 'F':
            y, x = y + dy, x + dx
            if dy > 0:
                max_y = max(max_y, y)
            else:
                min_y = min(min_y, y)
            if dx > 0:
                max_x = max(max_x, x)
            else:
                min_x = min(min_x, x)
        # 뒤로 이동
        elif r == 'B':
            y, x = y - dy, x - dx
            if dy > 0:
                min_y = min(min_y, y)
            else:
                max_y = max(max_y, y)
            if dx > 0:
                min_x = min(min_x, x)
            else:
                max_x = max(max_x, x)
        # 오른쪽으로 회전
        elif r == 'R':
            d = (d + 1) % 4
        # 왼쪽으로 회전
        else:
            if d == 0:
                d = 3
            else:
                d -= 1
    print((max_y - min_y) * (max_x - min_x))