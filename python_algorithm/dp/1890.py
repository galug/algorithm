# 점프
# N x N 칸에서 graph 에 갈 수 있는 거리가 적혀있다.
# 오른쪽, 아래칸으로만 이동해서 n-1, n-1 까지 도착하는 개수를 센다.
import sys


# 이동할 수 있는지 확인하는 함수
def can_movable(_y: int, _x: int) -> bool:
    if 0 <= _y < n and 0 <= _x < n:
        return True
    else:
        return False


# 값들을 입력받음
n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# dp 준비
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
# 아래, 오른쪽으로만 이동하기 때문에 반복문을 통한 dp가 가능하다.
for i in range(n):
    for j in range(n):
        # 이번 칸에서 이동할 수 있는 거리
        move_distance = graph[i][j]
        # 이동한 곳을 저장
        _i, _j = i + move_distance, j + move_distance
        # 도착
        if move_distance == 0:
            break
        # 현재 칸으로 왔던 적이 있어야 다음 칸으로 갈 수 있다.
        if dp[i][j]:
            # 이동 가능한 곳들이면 현재 칸으로 온 개수만큼 다음 칸으로 이동한다.
            if _i < n:
                dp[_i][j] += dp[i][j]
            if _j < n:
                dp[i][_j] += dp[i][j]

print(dp[n - 1][n - 1])
