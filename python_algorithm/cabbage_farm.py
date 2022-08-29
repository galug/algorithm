import sys
import collections
n = int(input())
results = []
def dfs(x:int, y:int,width, height, m):
    if x<0 or x>=width or y<0 or y>=height or m[y][x]==0:
        return
    m[y][x] = 0
    dfs(x, y+1,width, height, m)
    dfs(x, y-1, width, height, m)
    dfs(x+1, y, width, height, m)
    dfs(x-1, y, width, height, m)
for _ in range(n):
    width, height, cn = map(int,sys.stdin.readline().split())
    m = [[0]*width for _ in range(height)]
    cabbage = []
    result =0
    for _ in range(cn):
        x, y = map(int,sys.stdin.readline().split())
        m[y][x] = 1
        cabbage.append([x,y])
    for x,y in cabbage:
        if m[y][x] == 1:
            dfs(x, y, width, height, m)
            result += 1
    results.append(result)
for ele in results:
    print(ele)