import sys

n, m = map(int,sys.stdin.readline().split())
table = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for _ in range(m):
    x1,y1, x2, y2 = map(int,sys.stdin.readline().split())
    ans = 0
    