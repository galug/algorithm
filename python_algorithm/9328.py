import collections
import sys

t= int(input())
# def is_graph:
#     pass
def unlock():
    for i in range(h+2):
        for j in range(w+2):
            if i== 0 or i==h+1 or
for _ in range(t):
    h, w = map(int,sys.stdin.readline().split())
    graph = []
    q = collections.deque()
    answer = 0
    for i in range(h+2):
        if i == 0 or i==h+1:
            graph.append(['.']*(w+2))
        else:
            graph.append(['.'] + list(map(str, sys.stdin.readline().rstrip()))+['.'])
    key = list(map(str,sys.stdin.readline().rstrip()))
    while key:
        if key[0] == '0':
            break

    print(graph)