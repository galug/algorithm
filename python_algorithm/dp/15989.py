# 1,2,3 을 더해서 만들 수 있는 수열의 수를 구하라
MAX_NUM = 10_001
tc = int(input())
# 기본적으로 모든 수는 1로 구성 되어있다.
dp = [1] * MAX_NUM

# 모든 수는 (i-2) + 3 로 구성된다.
for i in range(2, MAX_NUM):
    dp[i] += dp[i - 2]
# 모든 수는 (i-3) + 3 으로 구성된다 .
for i in range(3, MAX_NUM):
    dp[i] += dp[i - 3]

for _ in range(tc):
    n = int(input())
    print(dp[n])
