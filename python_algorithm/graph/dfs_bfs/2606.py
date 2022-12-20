# 연결되어있는 노드의 개수를 출력하는 프로그램
import sys

# 정점의수, edge 의 수와 바이러스의 graph 를 입력받는다.
vertex = int(input())
edge = int(input())
graph = [[] for _ in range(vertex + 1)]
for _ in range(edge):
    vertex1, vertex2 = map(int, sys.stdin.readline().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

visited = {1}

# 방문한노드인지 확인한 후 방문 하지 않았을 시 방문 목록에 추가
def dfs(precedence_node):
    for v in graph[precedence_node]:
        if v not in visited:
            visited.add(v)
            dfs(v)


dfs(1)
print(len(visited) - 1)
