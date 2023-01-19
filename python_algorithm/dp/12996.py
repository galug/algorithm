# 문제 Acca
# S 개의 곡을 3 사람이 각각 d,k,h 개 씩 칠 때 나눠칠수 있는 경우의 수
import sys


def solution(remain_songs, d_song, k_song, h_song):
    # 남은 곡이 연주할 사람 보다 많거나 남은 곡의 숫자보다 사람이 많아지는 경우 0을 반환
    if remain_songs > d_song + k_song + h_song or remain_songs < d_song or remain_songs < k_song or remain_songs < h_song:
        return 0
    # dp 에 저장해놓은 경우 반환
    if dp[remain_songs][d_song][k_song][h_song] != 0:
        return dp[remain_songs][d_song][k_song][h_song]
    # 모든 곡을 연주한 경우 나머지를 제곱을 해서 경우의 수를 반환
    if remain_songs == 0:
        return (s ** d_song * s ** k_song * s ** h_song) % 1_000_000_007
    # 1곡을 연주할 수 있는 경우의 수들을 더 해준다. 총 7가지의 경우가 있음
    for _ds, _ks, _hs in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)):
        nds, nks, nhs = d_song - _ds, k_song - _ks, h_song - _hs
        if nds < 0 or nks < 0 or nhs < 0:
            continue
        dp[remain_songs][d_song][k_song][h_song] += (solution(remain_songs - 1, nds, nks, nhs) % 1_000_000_007)
    return dp[remain_songs][d_song][k_song][h_song]


s, d, k, h = map(int, sys.stdin.readline().split())
dp = [[[[0 for _ in range(h + 1)] for _ in range(k + 1)] for _ in range(d + 1)] for _ in range(s + 1)]
for ds, ks, hs in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)):
    dp[1][ds][ks][hs] = 1
start = max((d, k, h))
# 가능한 최소 곡의 수부터 다 정해준다.
for i in range(start, s + 1):
    solution(i, d, k, h)
print(dp[s][d][k][h]  % 1_000_000_007)
