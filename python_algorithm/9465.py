import sys

t = int(input())
answer = []
for _ in range(t):
    n = int(sys.stdin.readline())
    stickers = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    if n == 1:
        print(max(stickers[0][0],stickers[1][0]))
    elif n == 2:
        print(max(stickers[0][0]+stickers[1][1],stickers[1][0]+stickers[0][1]))
    else:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]
        for i in range(2, n):
            stickers[0][i] = max(stickers[1][i-1]+stickers[0][i], stickers[1][i-2]+stickers[0][i])
            stickers[1][i] = max(stickers[0][i-1]+stickers[1][i], stickers[0][i-2]+stickers[1][i])
        print(max(stickers[0][n-1],stickers[1][n-1]))