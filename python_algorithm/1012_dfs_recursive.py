import sys
sys.setrecursionlimit(50000)

def is_area(x:int,y:int, field:list):
    if x<0 or x >=len(field[0]) or y<0 or y>= len(field) or field[y][x] != 1:
        return
    field[y][x] = 0
    is_area(x - 1,y ,field)
    is_area(x + 1, y, field)
    is_area(x, y - 1, field)
    is_area(x, y + 1, field)


t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    M, N , K = map(int,sys.stdin.readline().split())
    field = [[0]*M for _ in range(N)]
    a = 0
    for K in range(K):
        x,y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                is_area(j, i, field)
                a += 1
    answer.append(a)
for ele in answer:
    print(ele)