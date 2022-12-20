import collections
import sys

N, M = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
red_ball = []
blue_ball = []
ew = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs():
    q = collections.deque([[red_ball, blue_ball,0]])
    visited = []
    while q:
        red, blue, move = q.popleft()
        if move>=10:
            continue
        ry, rx = red[0], red[1]
        by, bx = blue[0], blue[1]
        for py,px in ew:
            i, j = 1, 1
            while graph[ry+py*i][rx+px*i] not in '#O':
                i += 1
            while graph[by+py*j][bx+px*j] not in '#O':
                j += 1
            i -= 1
            j-=1
            if ry + py* i == by +py *j and rx + px * i == bx + px * j:
                if graph[ry+py*(i+1)][rx+px*(i+1)] == 'O':
                    continue
                if i <j:
                    j-=1
                else:
                    i -= 1
            if graph[ry + py * (i+1)][rx + px * (i+1)] == 'O':
                print(move+1)
                return
            if (i==0 and j==0) or graph[by+py*(j+1)][bx+px*(j+1)] == 'O':
                continue
            if [ry + py * i,rx + px * i,by + py * j,bx + px * j] not in visited:
                visited.append([ry + py * i,rx + px * i,by + py * j,bx + px * j])
                q.append([[ry+py*i,rx+px*i],[by+py*j, bx+px*j],move+1])
    print(-1)
    return
for i in range(1,N-1):
    for j in range(1,M-1):
        if graph[i][j] == 'R':
            red_ball = [i,j]
        elif graph[i][j] == 'B':
            blue_ball = [i,j]
bfs()