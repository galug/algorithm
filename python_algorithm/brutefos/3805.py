# 애니팡 1번의 이동으로 최대 개수를 지울 수 있는 경우를 센다.
import sys

direct_y = [1, 0, -1, 0]
direct_x = [0, 1, 0, -1]
n = int(input())

graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

# 사탕 내에서 가장 긴 터지는 줄을 찾아주는 함수
def find_max_same_candi_length():
    max_length = 0
    for y in range(n):
        for x in range(n):
            for i in range(4):
                move_y = direct_y[i]
                move_x = direct_x[i]
                if validate(y, x, move_y, move_x):
                    change(y, x, move_y, move_x)
                    same_candi = compare_candi_row(y, x)
                    change(y, x, move_y, move_x)
                    max_length = max(max_length, same_candi)
            if max_length == n:
                return max_length
    return max_length

# 그래프 내에 유효하게 존재하는지 확인하는 함수
def validate(y, x, move_y, move_x):
    return 0 <= y + move_y < n and 0 <= x + move_x < n

# 사탕의 위치를 바꿔주는 함수
def change(y, x, move_y, move_x):
    original = graph[y][x]
    graph[y][x] = graph[y + move_y][x + move_x]
    graph[y + move_y][x + move_x] = original

# 가로와 세로 중 더 길게 터지는 줄을 반환해주는 함수
def compare_candi_row(y, x):
    vertical = compare_candi_vertical(y, x)
    horizontal = compare_candi_horizontal(y, x)
    return max(vertical, horizontal)

# 세로의 캔디를 비교해주는 함수
def compare_candi_vertical(y, x):
    plus_vertical = 0
    minus_vertical = 0
    while compare_candi(y, x, plus_vertical, 0):
        plus_vertical += 1
    while compare_candi(y, x, minus_vertical * -1, 0):
        minus_vertical += 1
    return plus_vertical + minus_vertical - 1

# 가로의 캔디를 비교해주는 함수
def compare_candi_horizontal(y, x):
    plus_horizontal = 0
    minus_horizontal = 0
    while compare_candi(y, x, 0, plus_horizontal):
        plus_horizontal += 1
    while compare_candi(y, x, 0, minus_horizontal * -1):
        minus_horizontal += 1
    return plus_horizontal + minus_horizontal - 1

# 캔디가 같은지 비교하는 함수
def compare_candi(y, x, move_y, move_x):
    if not validate(y, x, move_y, move_x):
        return False
    return graph[y][x] == graph[y + move_y][x + move_x]


print(find_max_same_candi_length())
