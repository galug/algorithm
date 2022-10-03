import heapq
import sys

V,E = map(int,sys.stdin.readline().split())

edges = []
parent = [i for i in range(V+1)]
answer = 0
for _ in range(E):
    A, B, C = map(int,sys.stdin.readline().split())
    edges.append([C, A, B])
edges.sort()
def get_parent(x):
    if x == parent[x]:
        return x
    else:
        return get_parent(parent[x])
def find_union(a, b):
    p1 = get_parent(a)
    p2 = get_parent(b)
    if p1 == p2:
        return True
    return False
def union_set(a,b):
    p1 = get_parent(a)
    p2 = get_parent(b)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2
for c, a, b in edges:
    if not find_union(a,b):
        union_set(a,b)
        answer += c
print(answer)