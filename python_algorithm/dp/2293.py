# 주어진 동전들을 이용해서 원하는 값을 만들어낼 수 있는 경우의 수를 구하자.
import sys

# 코인 개수와 만들 가격 입력
n, k = map(int, sys.stdin.readline().split())

# 코인들을 저장하고 정렬한다.
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

# 다이나믹 프로그래밍 준비
dp = [0] * (k + 1)
# 가격이 0인 경우에는 1개는 무조건 확보이다.
dp[0] = 1

# dp[i(각각의 동전의 경우)][j(가치의 합)]
# = dp[i-1(지금 전 동전의 경우)][j] + coins[i][j - coins[i](지금 화폐 가치만큼 하나 집어넣는 경우)]
for i in range(n):
    for j in range(k + 1):
        if j >= coins[i]:
            dp[j] += dp[j - coins[i]]
print(dp[k])
