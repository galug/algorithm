import heapq
import sys


N,M = map(int,sys.stdin.readline().split())
box = [list(map(int,sys.stdin.readline().split()))for _ in range(M)]

def in_box(i, j) -> bool:
    if i<0 or i>=M or j<0 or j>=N or box[i][j] != 0:
        return False
    return True
def bfs():
    heap = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    max_days = 0
    for i in range(M):
        for j in range(N):
            if box[i][j] == 1:
                heapq.heappush(heap,[0,i,j])
    while heap:
        days, y, x = heapq.heappop(heap)
        max_days = max(days,max_days)
        for i in range(4):
            if in_box(y+dy[i],x+dx[i]):
                box[y+dy[i]][x+dx[i]] = 1
                heapq.heappush(heap,[days+1, y+dy[i], x+dx[i]])
    for i in range(M):
        for j in range(N):
            if box[i][j] == 0:
                print(-1)
                return
    print(max_days)
bfs()