import sys

def is_in_area(x,y,field):
    if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field) or field[y][x] != 1:
        return False
    return True
def is_area_iterative(x:int,y:int, field:list):
    stack = [[y,x]]
    ew = [[0,1],[0,-1],[1,0],[-1,0]]
    while stack:
        y, x = stack.pop()
        field[y][x] =0
        for _ in range(4):
            if is_in_area(x+1, y, field): stack.append([y, x+1])
            if is_in_area(x-1, y, field): stack.append([y, x-1])
            if is_in_area(x, y + 1, field): stack.append([y+1, x])
            if is_in_area(x, y - 1, field): stack.append([y -1, x])
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
                is_area_iterative(j, i, field)
                a += 1
    answer.append(a)
for ele in answer:
    print(ele)