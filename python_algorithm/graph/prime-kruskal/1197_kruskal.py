#
# MST 를 구하는 알고리즘
# 크루스칼 알고리즘이다. 

import sys

V, E = map(int, sys.stdin.readline().split())

# 간선들을 오름 차순으로 정렬해준다.

edges = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append([C, A, B])
edges.sort()

# 같은 사이클 내에 있는 node 들의 부모를 찾다보면 같은 부모를 가지게 된다.
parent = [i for i in range(V + 1)]


# 두 자식이 같은 사이클 안에 있는지 확인한다.
def find_union(child1, child2):
    p1 = get_parent(child1)
    p2 = get_parent(child2)
    if p1 == p2:
        return True
    return False


# 자식의 부모를 찾는다.
def get_parent(x):
    # 부모의 경우 자신의 부모 = 자신 이 된다.
    if x == parent[x]:
        return x
    else:
        return get_parent(parent[x])


# 2개의 서로 다른 사이클이 합쳐지는 과정이다.
def union_set(child1, child2):
    p1 = get_parent(child1)
    p2 = get_parent(child2)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2


answer = 0

for c, a, b in edges:
    if not find_union(a, b):
        union_set(a, b)
        answer += c

print(answer)
