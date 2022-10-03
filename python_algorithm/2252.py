import collections
import sys

n, m = map(int,sys.stdin.readline().split())
q = collections.deque()
graph = [[] for _ in range(n+1)]
in_deed = [0]*(n+1)
answer = []
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[b].append(a)
    in_deed[a] += 1
for i in range(1,n+1):
    if in_deed[i] == 0:
        q.append(i)
        answer.append(i)
while q:
    for v in graph[q.popleft()]:
        in_deed[v] -= 1
        if in_deed[v] == 0:
            q.append(v)
            answer.append(v)
print(' '.join(map(str,answer[::-1])))