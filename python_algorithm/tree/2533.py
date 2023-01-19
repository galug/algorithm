# dp 와 트리를 활용한 문제
import collections
import sys

sys.setrecursionlimit(1000000)


def dfs(n: int):
    # 부모 노드를 다시 방문하지 않게 방문한 노드를 기록
    visited.add(n)
    # 본인을 얼리어 답터의 수에 포함
    dp[n][1] = 1
    for child_node in edges[n]:
        # 현 노드의 자식 노드들 중에서
        if child_node not in visited:
            # 다시 dfs 들어가기
            dfs(child_node)
            # 본인이 얼리어 답터가 아닐 시 자식들이 얼리어 답터인 경우만 더해야함
            dp[n][0] += dp[child_node][1]
            # 본인이 얼리어 답터일시 자식은 얼리어답터든 아니든 상관 없음
            dp[n][1] += min(dp[child_node][0], dp[child_node][1])


number_of_nodes = int(input())
edges = collections.defaultdict(list)
# edges 들에 부모 자식 간의 간선 그려넣음
for _ in range(number_of_nodes - 1):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)
# dp 와 visited 준비
dp = [[0, 0] for _ in range(number_of_nodes + 1)]
visited = set()
# 1을 루트노드로 깊이 우선탐색
dfs(1)
# 루트노드가 얼리어답터인 경우와 얼리어 답터가 아닌 경우 중 더 작은 값이 정답 
print(min(dp[1][0], dp[1][1]))