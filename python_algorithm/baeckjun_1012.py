def dfs(i, j):
    if i<0 or i>=N or j>=M or j<0:
        return
    if farm[i][j]==0:
        return
    farm[i][j] = 0
    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)


case_num = int(input())
answer =[]
for _ in range(case_num):
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    count = 0
    for _ in range(K):
        w, h = map(int,input().split())
        farm[h][w] = 1
    for i in range(N):
        for j in range(M):
            if farm[i][j]==1:
                dfs(i,j)
                count += 1
    answer.append(count)
for a in answer:
    print(a)