import collections

N, K = map(int,input().split())
q = collections.deque()
q.append(N)
pMax = 100000
dist = [0]* (pMax+1)
while q:
    x = q.popleft()
    if x == K:
        print(dist[x])
        break
    for nx in (x+1, x-1, x*2):
        if 0<=nx<pMax and not dist[nx]:
            dist[nx] = dist[x]+1
            q.append(nx)
