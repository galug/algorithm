import sys

n = int(input())
it = list(map(int, sys.stdin.readline().split()))
dp = [1]
for i in range(1,len(it)):
    temp = it[i]
    max_j = 0
    for j in range(i):
        if it[j] < temp:
            max_j = max(dp[j], max_j)
    dp.append(max_j+1)
print(max(dp))