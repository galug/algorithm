import sys

def is_onepaper(i,j,n,p:list) -> bool:
    mzp = p[i][j]
    for k in range(i, i+n):
        for l in range(j, j+n):
            if mzp != p[k][l]:
                return False
    return True
def dfs(i,j,n,p):
    if is_onepaper(i,j,n,p):
        answer[p[i][j]+1] +=1
        return
    temp = n//3
    for k in (i,i +temp, i + temp*2):
        for l in (j, j+temp,j + temp*2):
            dfs(k,l,temp,p)
N = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer = [0,0,0]
dfs(0,0,N,paper)
for ele in answer:
    print(ele)