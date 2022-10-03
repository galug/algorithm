import collections
import sys

N, M = map(int,sys.stdin.readline().split())
graph = collections.defaultdict(list)
in_deed = [0]*(N+1)
que = collections.deque()
answer = []
for _ in range(M):
    order = list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(order)):
        # 뒤에 몇 명 서는지 저장
        if i!= len(order)-1:
            in_deed[order[i]] += 1
        if i!= 1:
            graph[order[i]].append(order[i-1])
for i in range(1,N+1):
    if in_deed[i] == 0:
        que.append(i)
while que:
    et = que.popleft()
    answer.append(et)
    while graph[et]:
        ele = graph[et].pop()
        in_deed[ele] -= 1
        if in_deed[ele] == 0:
            que.append(ele)
if len(answer) != N:
    print(0)
else:
    for i in range(N-1,-1,-1):
        print(answer[i])