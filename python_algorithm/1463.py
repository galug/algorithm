n = int(input())
dp = {1:0, 2:1}
def dfs(n):
    if n in dp: return dp[n]
    dp[n] = min(dfs(n//2)+n%2, dfs(n//3)+n%3)+1
    return dp[n]
print(dfs(n))
