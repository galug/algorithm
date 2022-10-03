# dp 와 비트 마스킹을 이용한 해밀턴 순환 문제 풀이
import sys

n = int(input())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
