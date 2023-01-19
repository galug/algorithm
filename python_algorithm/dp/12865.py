# 배낭에 넣을 수 있는 최대 가치 문제
import sys

# n 개의 물건을 받고 최대 K 만큼의 무게만 넣을 수 있는 배낭에 넣는다.
n, k = map(int, sys.stdin.readline().split())
# 무게 0 의 key 에 0의 value 가 들어가 있음
dp = {0: 0}

# O(n^^2) 이 된다.
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    new_dp = {}
    # 기존에 있는 물건들의 합 중에서
    for value, weight in dp.items():
        # 가치가 동일하거나 동일한 가치의 물건이 없을 때 기존물건 무게 + 새 물건 무게 < 기존에 존재하는 같은 가치의 조합의 무게(부재 시 수용 가능 무게)
        if weight + w < dp.get(value + v, k + 1):
            new_dp[value + v] = weight + w
    dp.update(new_dp)

print(max(dp.keys()))
