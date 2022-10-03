# meet in the middle 을 활용
# 반으로 쪼개서 수열들의 합을 한 번 확인
import collections
import sys


def dfs_left(start, ts):
    if start!= 0:
        if ts == K:
            answer[0] +=1
        result_left[ts] += 1
    for i in range(start, N // 2):
        dfs_left(i + 1, ts + l[i])

def dfs_right(start, ts):
    if start!= N//2:
        if ts == K:
            answer[0] +=1
        if result_left[K-ts]:
            answer[0] += result_left[K-ts]
    for i in range(start, N):
        dfs_right(i + 1, ts + l[i])

N, K = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
result_left = collections.defaultdict(int)
result_right = collections.defaultdict(int)

answer = [0]
dfs_left(0, 0)
dfs_right(N // 2, 0)
print(answer[0])