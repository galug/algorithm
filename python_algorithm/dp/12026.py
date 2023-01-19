# BOJ 거리
import sys
# 입력 받기
n = int(input())
blocks = list(map(str, sys.stdin.readline().rstrip()))
boj = {'B': 0, 'O': 1, 'J': 2}
# dp 를 나타낸다.
dp = [float('inf')] * n
dp[0] = 0
# O(n^^2)
for i in range(n):
    block = boj[blocks[i]]
    # 다음 단계로 갈 방법이 있는지 탐색한다.
    for j in range(i + 1, n):
        # 블록들 중 다음 블록으로 이동 
        if boj[blocks[j]] == (block + 1) % 3:
            dp[j] = min(dp[j], dp[i] + (i - j) * (i - j))
if dp[j] == float('inf'):
    print(-1)
else:
    print(dp[n - 1])

