import sys

def is_onepaper(i,j,n):
    oz = paper[i][j]
    for k in range(i,i+n):
        for l in range(j,j+n):
            if paper[k][l] != oz:
                return False
    return True
def dfs(i, j, n):
    if is_onepaper(i,j,n):
        answer[paper[i][j]] += 1
        return
    half = n//2
    dfs(i, j, half)
    dfs(i+half, j, half)
    dfs(i, j+half, half)
    dfs(i+half, j+half, half)

n = int(input())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer= [0,0]
dfs(0,0,n)
print(str(answer[0])+'\n'+str(answer[1]))