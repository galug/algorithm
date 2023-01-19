import sys


def is_Palindrome(s, e):
    if seq[s:e + 1] == seq[e, s - 1, -1]:
        return True
    return False


N = int(input())
seq = [0] + list(map(int, sys.stdin.readline().split()))
M = int(input())
dp = [[False] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][i] = True

for j in range(N + 1):
    for i in range(N + 1):
        if i == 0 or j == 0 or i == j or i > j:
            dp[i][j] = True
            continue
        else:
            if j == i + 1:
                if seq[i] == seq[j]:
                    dp[i][j] = True
                    continue
            if dp[i + 1][j - 1]:
                if seq[i] == seq[j]:
                    dp[i][j] = True
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if dp[start][end]:
        print(1)
    else:
        print(0)
