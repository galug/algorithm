# 데스 노트
# 써야할 사람과 가로 칸의 수 입력 받기
import sys

sys.setrecursionlimit(1000000)


def dfs(cur_idx, total):
    line_sum = names[cur_idx]
    i = cur_idx + 1
    while i < n:
        if line_sum + names[i] + 1 <= horizontal:
            line_sum += (names[i] + 1)
            i += 1
        else:
            break
    print(cur_idx, i, total)
    if i == n:
        global answer
        answer = min(answer, total)
        return
    if dp[cur_idx][line_sum] == 0:
        dp[cur_idx][line_sum] = 1
        dfs(i, total + (horizontal - line_sum) * (horizontal - line_sum))
    if dp[cur_idx][line_sum - (names[i - 1] + 1)] == 0:
        line_sum -= (names[i - 1] + 1)
        dp[cur_idx][line_sum] = 1
        dfs(i - 1, total + (horizontal - line_sum) * (horizontal - line_sum))


# 죽일 사람의 수와 가로줄의 수를 입력받음
n, horizontal = map(int, sys.stdin.readline().split())
# 이름의 길이들을 입력받음
names = [int(input()) for _ in range(n)]

answer = sys.maxsize
dp = [[0] * 1001 for _ in range(1001)]

if n == 1:
    print((horizontal - names[0]) * (horizontal - names[0]))
else:
    dfs(0, 0)
    print(answer)
