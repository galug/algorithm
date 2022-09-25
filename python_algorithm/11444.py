num = int(input())
dp = [0]*(num+1)
dp[1],dp[2] = 1, 1
def dfs(n):
    if n==0:
        return 0
    if dp[n]:
        return dp[n]
    return dfs(n-1) + dfs(n-2)
print(dfs(num)%1000000007)
