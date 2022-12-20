# 그래프를 DFS와 BFS로 탐색한 결과
import collections
import sys

# 정점수, 간선 수, 시작 정점을 입력 받고 그래프에 넣는다.
number_of_vertex, number_of_edge, start_vertex = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(number_of_vertex + 1)]
for _ in range(number_of_edge):
    vertex1, vertex2 = map(int, sys.stdin.readline().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)
# 그래프를 숫자 순서로 정렬
for i in range(1, number_of_vertex + 1):
    graph[i].sort()
# 방문 순서를 저장할 리스트
visited_dfs = [start_vertex]
visited_bfs = [start_vertex]

# 깊이 우선 탐색
def dfs(start):
    if len(visited_dfs) == number_of_vertex:
        return
    for vertex in graph[start]:
        if vertex not in visited_dfs:
            visited_dfs.append(vertex)
            dfs(vertex)

# 넓이 우선 탐색
def bfs(start):
    que = collections.deque([start])
    while que and len(visited_bfs) != number_of_vertex:
        find_vertex = que.popleft()
        for vertex in graph[find_vertex]:
            if vertex not in visited_bfs:
                visited_bfs.append(vertex)
                que.append(vertex)


dfs(start_vertex)
bfs(start_vertex)

for a in visited_dfs:
    print(a, end=' ')
print()
for a in visited_bfs:
    print(a, end=' ')
