import sys

n = int(input())

# rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# if n==1:
#     print(min(rgb[0]))
# else:
#     for i in range(1,len(rgb)):
#         for j in range(3):
#             if j == 0:
#                 min_num = min(rgb[i-1][1],rgb[i-1][2])
#             elif j == 1:
#                 min_num = min(rgb[i - 1][0], rgb[i - 1][2])
#             else:
#                 min_num = min(rgb[i - 1][0], rgb[i - 1][1])
#             rgb[i][j] += min_num
# print(min(rgb[n-1]))

dp = [list(map(int,sys.stdin.readline().split()))]
for i in range(1,n):
    r, g, b = map(int,sys.stdin.readline().split())
    nr = r + min(dp[i-1][1],dp[i-1][2])
    ng = g + min(dp[i-1][0],dp[i-1][2])
    nb = b + min(dp[i-1][1],dp[i-1][0])
    dp.append([nr,ng,nb])
print(min(dp[n-1]))