import collections
import sys
sys.setrecursionlimit(100000)
n = int(input())
graph = collections.defaultdict(list)
for _ in range(n):
    parent, left, right = map(str, sys.stdin.readline().split())
    graph[parent].append(left)
    graph[parent].append(right)
def inorder(v):
    if len(graph[v])==0 or v =='.':
        return
    inorder(graph[v][0])
    print(v,end='')
    inorder(graph[v][1])

def preorder(v):
    if len(graph[v])==0 or v =='.':
        return
    print(v, end='')
    preorder(graph[v][0])
    preorder(graph[v][1])


def outorder(v):
    if len(graph[v])==0 or v =='.':
        return
    outorder(graph[v][0])
    outorder(graph[v][1])
    print(v, end='')
preorder('A')
print()
inorder('A')
print()
outorder('A')