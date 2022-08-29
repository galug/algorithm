import sys
import collections
n = int(input())
results = []
def is_valid(x:int, y:int, width, height, m):
    if x<0 or x>=width or y<0 or y>=height or m[y][x]==0:
        return False
    else:
        return True

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
            q = collections.deque([x, y])
            while q:
                tx, ty = q.popleft()
                if m[ty][tx] == 1:
                    m[ty][tx] = 0
                if is_valid(tx + 1, ty, width, height, m): q.append([tx + 1, ty])
                if is_valid(tx - 1, ty, width, height, m): q.append([tx - 1, ty])
                if is_valid(tx, ty + 1, width, height, m): q.append([tx, ty + 1])
                if is_valid(tx, ty - 1, width, height, m): q.append([tx, ty - 1])
            result += 1
    print(result)