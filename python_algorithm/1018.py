import sys

N, M = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(N)]
result = sys.maxsize
for h in range(N-7):
    for k in range(M-7):
        resulta = 0
        resultb = 0
        for i in range(h, h+8):
            for j in range(k, k+8):
                if ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)):
                    if (board[i][j] == 'B'):
                        resulta += 1
                    else:
                        resultb += 1
                else:
                    if (board[i][j] == 'W'):
                        resulta += 1
                    else:
                        resultb += 1
        result = min(resulta,result,resultb)
print(result)
