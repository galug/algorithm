import sys

N, M = map(int,sys.stdin.readline().split())
dic = {}
for i in range(1,N+1):
    poketmon = sys.stdin.readline().split()
    dic[poketmon] = i
    dic[i] = poketmon
for i in range(M):
    ans = sys.stdin.readline().split()
    if ans.isdigit():
        print(dic[int(ans)])
    else:
        print(dic[ans])