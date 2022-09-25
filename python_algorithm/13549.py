import collections
import sys

n, k = map(int, sys.stdin.readline().split())
q = collections.deque([n])
visited = {}
visited[n] = 0
while q:
    x = q.popleft()
    if k in visited:
        print(visited[k])
        break
    if x > k and x-1 not in visited:
        q.append(x-1)
        visited[x-1] = visited[x] +1
        continue
    if x - 1 >=0 and (x-1 not in visited):
        q.append(x-1)
        visited[x - 1] = visited[x] + 1
    if (x*2 <=100000) and (x*2 not in visited):
        q.append(x*2)
        visited[x * 2] = visited[x]
    if x+1 <=100000 and (x+1 not in visited):
        q.append(x+1)
        visited[x + 1] = visited[x] + 1


