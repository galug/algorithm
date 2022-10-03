import collections
import sys

sdoku = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
area = [[[0, 0], [0, 3], [0, 6]],
        [[3, 0], [3, 3], [3, 6]],
        [[6, 0], [6, 3], [6, 6]]]
zero = []
answer = [False]
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zero.append([i, j])

def can_in(k, l, num):
    if num in sdoku[k]:
        return False
    for i in range(9):
        if sdoku[i][l] == num:
            return False
    y, x = area[k // 3][l // 3][0], area[k // 3][l // 3][1]
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if sdoku[i][j] == num:
                return False
    return True

def dfs(n):
    if n == len(zero):
        answer[0] = True
        return True
    y, x = zero[n]
    for j in range(1, 10):
        if can_in(y, x, j):
            sdoku[y][x] = j
            dfs(n + 1)
            if(answer[0]):
                return
            sdoku[y][x] = 0
    return False
dfs(0)
for i in range(9):
    for j in range(9):
        print(sdoku[i][j],end='')
    print()