# tree + dp 문제
import sys

sys.setrecursionlimit(100000)

# 트리 문제이므로 재귀적인 접근 필요
def dfs(town):
    # 부모 노드를 다시 방문하지 않기 위한 코드
    visited.add(town)
    for next_town in edges[town]:
        # 자식 노드 중에서
        if next_town not in visited:
            # 재귀적 접근
            dfs(next_town)
            # 본인이 일반마을일시 자식은 우수 마을이던 일반 마을이던 상관 x
            # 인접한 우수 마을이 없는 경우는 max 값을 구하기 때문에 있을 수 없음
            # 인접한 3개의 노드 중 최소 1개의 노드는 선택해야 최대수가 될 수 있기 때문이다.
            dp[town][0] += max(dp[next_town][1], dp[next_town][0])
            # 본인이 우수 마을이면 자식들은 반드시 일반마을
            dp[town][1] += dp[next_town][0]

# 문제에 필요한 입력값 받는다.
number_of_town = int(input())
number_of_inhabits = [0] + list(map(int, sys.stdin.readline().split()))
edges = [[] for _ in range(number_of_town + 1)]
dp = [[0, number_of_inhabits[i]] for i in range(number_of_town + 1)]
for _ in range(number_of_town - 1):
    town1, town2 = map(int, sys.stdin.readline().split())
    edges[town1].append(town2)
    edges[town2].append(town1)

visited = set()
# 1을 기준으로 dfs
dfs(1)
print(max(dp[1][0], dp[1][1]))
