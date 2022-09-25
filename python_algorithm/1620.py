import collections
import sys

N, M = map(int,sys.stdin.readline().split())
dict = collections.defaultdict()
i = 1
for _ in range(N):
    pocketmon = sys.stdin.readline().rstrip()
    dict[pocketmon] = str(i)
    dict[str(i)] = pocketmon
    i+=1
for _ in range(M):
    q = sys.stdin.readline().rstrip()
    print(dict[q])
