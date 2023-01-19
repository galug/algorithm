# 괄호의 개수는 카탈란 수를 이룬다.
# 카탈란 수에 대해서 찾아보기
tc = int(input())
dp = [0] * 5_001
dp[0] = 1
dp[2] = 1

# 점화식은 dp[n] = dp[n-i] * dp[i] for i in range(n) 을 이룬다. 
for i in range(4, 5_001, 2):
    for j in range(0, i, 2):
        dp[i] += (dp[j] * dp[i - j - 2])
        dp[i] %= 1_000_000_007

for _ in range(tc):
    length = int(input())
    if length % 2 == 1:
        print(0)
        continue
    print(dp[length])
