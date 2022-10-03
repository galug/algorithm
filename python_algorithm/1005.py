import collections
import sys

t = int(input())
for _ in range(t):
    N, K = map(int,sys.stdin.readline().split())
    resources = [0] + list(map(int,sys.stdin.readline().split()))
    in_deed = [0] * (N+1)
    q = collections.deque()
    graph = collections.defaultdict(list)
    dp = [0] * (N + 1)
    for _ in range(K):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        in_deed[e] +=1
    for i in range(1,N+1):
        if in_deed[i] ==0:
            q.append(i)
            dp[i] = resources[i]
    while q:
        nxt = q.popleft()
        for v in graph[nxt]:
            in_deed[v] -= 1
            dp[v] = max(dp[v],resources[v] + dp[nxt])
            if in_deed[v] == 0:
                q.append(v)
    end = int(input())
    print(dp[end])
