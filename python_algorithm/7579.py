import sys

N, M = map(int,sys.stdin.readline().split())
active_memory = list(map(int,sys.stdin.readline().split()))
inactive_memory = list(map(int,sys.stdin.readline().split()))
total = sum(inactive_memory)
dp = [[0]*(sum(inactive_memory)+1) for _ in range(N+1)]
answer = sys.maxsize
for i in range(N+1):
    for j in range(total + 1):
        if i== 0:
            continue
        if inactive_memory[i-1] <=j:
            dp[i][j] = max(dp[i][j],dp[i-1][j-inactive_memory[i-1]]+active_memory[i-1])
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] >= M and j < answer:
            answer = j

print(answer)