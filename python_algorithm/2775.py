import sys

t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    l = [i for i in range(1,n+1)]
    for j in range(k):
        for h in range(n):
            if h == 0:
                continue
            else:
                l[h] += l[h-1]
    answer.append(l[-1])
for ele in answer:
    print(ele)