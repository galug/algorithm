import sys

n = int(input())
l = []
answer = []
for i in range(n):
    w, h = map(int,sys.stdin.readline().split())
    l.append((w,h))
for i in range(n):
    rank = 1
    for j in range(n):
        if l[i][0] <l[j][0] and l[i][1] < l[j][1]:
            rank+=1
    answer.append(rank)
for ele in answer:
    print(ele)