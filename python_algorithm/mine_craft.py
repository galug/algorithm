from collections import Counter

N,M,B= map(int,input().split())
ct=Counter()
s: int  = 0
avg: int  = 0
for _ in range(N):
    l=list(map(int,input().split()))
    ct.update(l)
for k in ct.keys():
    s += k*ct[k]
avg = s
s = s+ B