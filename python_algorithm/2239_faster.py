import collections
import sys

sdoku = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
zero = []
answer = [False]
row = collections.defaultdict(list)
column = collections.defaultdict(list)
nine = collections.defaultdict(list)
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zero.append([i, j])
        else:
            row[i].append(sdoku[i][j])
            column[j].append(sdoku[i][j])
            nine[(i//3)*3+(j//3)].append(sdoku[i][j])

def can_in(k, l, num):
    if num in row[k]:
        return False
    if num in column[l]:
        return False
    if num in nine[(i//3)*3+(j//3)]:
        return False
    return True

def dfs(n):
    if n == len(zero):
        answer[0] = True
        return True
    y, x = zero[n]
    print(sdoku)
    for j in range(1, 10):
        if can_in(y, x, j):
            sdoku[y][x] = j
            row[y].append(j)
            column[x].append(j)
            nine[(y // 3) * 3 + (x // 3)].append(j)
            dfs(n + 1)
            if(answer[0]):
                return
            sdoku[y][x] = 0
            row[y].remove(j)
            column[x].remove(j)
            nine[(y // 3) * 3 + (x // 3)].remove(j)
    return False
dfs(0)
for i in range(9):
    for j in range(9):
        print(sdoku[i][j],end='')
    print()