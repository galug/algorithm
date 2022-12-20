# topology sort
import collections
import sys

n, m = map(int, sys.stdin.readline().split())

# 각 사람의 진입 차수의 개수를 세는 리스트
in_degree_list = [0] * (n + 1)
# 뒤의 사람(진출 차수 노드)을 저장하는 리스트
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    out_degree, in_degree, = map(int, sys.stdin.readline().split())
    in_degree_list[in_degree] += 1
    graph[out_degree].append(in_degree)

answer = []
q = collections.deque()

# 들어오는 사람이 없는 진입 차수 저장
for i in range(1, n + 1):
    if in_degree_list[i] == 0:
        q.append(i)
        answer.append(i)

# 진입 차수가 없는 사람들을 sort 과정에서 제외한다.
while q:
    for child in graph[q.popleft()]:
        in_degree_list[child] -= 1
        # 진입 차수가 없는 child 이면 그 다음으로 키가 큰 사람이 된다.
        if in_degree_list[child] == 0:
            answer.append(child)
            q.append(child)

print(' '.join(map(str, answer)))
