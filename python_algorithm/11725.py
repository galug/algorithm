import collections
import sys

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    v,w = map(int,sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)
q = collections.deque([1])
answer = [0]*(n+1)
while q:
    node = q.popleft()
    for ele in graph[node]:
        if answer[ele] == 0:
            answer[ele] = node
            q.append(ele)
for i in range(2,n+1):
    print(answer[i])
