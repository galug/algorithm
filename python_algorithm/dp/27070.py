# 파이프 옮기기
# 제한된 이동 범위로만 이동 가능한 파이프를 목적지까지 옮길수 있는 경우의 수
import sys

n = int(input())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def can_move(y, x) -> bool:
    return graph[y][x] == 0


def can_move_diagonal(y, x) -> bool:
    return graph[y - 1][x] == 0 and graph[y][x - 1] == 0 and graph[y][x] == 0


HORIZONTAL = 0
VERTICAL = 1
DIAGONAL = 2

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
# 가로들은 모두 갈 수 있는 걸로 처리
for i in range(2, n):
    if graph[0][i] == 0:
        dp[HORIZONTAL][0][i] = dp[HORIZONTAL][0][i - 1]

# 그 전에 갈수 있었던 공간이 있었는지 판단하는 것이 포인트
for i in range(1, n):
    for j in range(1, n):
        if can_move_diagonal(i, j):
            dp[DIAGONAL][i][j] = sum(dp[direction][i - 1][j - 1] for direction in range(3))
        if can_move(i, j):
            dp[VERTICAL][i][j] = dp[VERTICAL][i - 1][j] + dp[DIAGONAL][i - 1][j]
            dp[HORIZONTAL][i][j] = dp[HORIZONTAL][i][j - 1] + dp[DIAGONAL][i][j - 1]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))
