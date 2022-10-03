import sys

n, m = map(int,sys.stdin.readline().split())
table = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            continue
        if i == 1 and j==1:
            dp[i][j] = table[i][j]
        elif i == 1:
            dp[i][j] = dp[i][j-1] +table[i][j]
        elif j == 1:
            dp[i][j] = dp[i-1][j] + table[i][j]
        else:
            dp[i][j] = dp[i-1][j]+dp[i][j-1] - dp[i-1][j-1]+table[i][j]
print(dp)
for _ in range(m):
    x1,y1, x2, y2 = map(int,sys.stdin.readline().split())
    x1,y1, x2, y2 = x1,y1, x2, y2
    ans = dp[x2][y2] -dp[x2][y1-1] + table[x1-1][y1-1]
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x2-1][y2-1])