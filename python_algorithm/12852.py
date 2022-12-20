import collections

n = int(input())
dp = [float('inf')] *(n+1)
prev = [-1] *(n+1)
dp[n] = 0
prev[n] = n
q = collections.deque([n])
while q:
    new = q.popleft()
    if new ==1:
        break
    if new // 3 >=1 and new % 3 == 0 and dp[new//3] > dp[new]+ 1 :
        dp[new//3] = dp[new] + 1
        prev[new//3] = new
        q.append(new//3)
    if new // 2 >=1 and new % 2 == 0 and dp[new//2] > dp[new]+ 1:
        dp[new//2] = dp[new] + 1
        prev[new//2] = new
        q.append(new//2)
    if dp[new-1] > dp[new]+1:
        dp[new-1] = dp[new] + 1
        prev[new-1] = new
        q.append(new-1)
print(dp[1])
t = 1
answer = []
while t != n:
    answer.append(t)
    t = prev[t]
answer.append(t)
answer.reverse()
print(' '.join(map(str,answer)))