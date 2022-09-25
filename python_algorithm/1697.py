import collections
import sys

N, K = map(int,sys.stdin.readline().split())
que = collections.deque()
que.append(N)
MAX = 100000
graph = [0] *(MAX+1)
while que:
    popleft = que.popleft()
    if popleft == K:
        print(graph[popleft])
        break
    for j in (popleft-1,popleft+1,popleft*2):
        if 0 <= j <= MAX and graph[j] == 0:
            que.append(j)
            graph[j] = graph[popleft]+1
