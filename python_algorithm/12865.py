import heapq
import sys

n,k = map(int,sys.stdin.readline().split())
cargo = []
for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    cargo.append([w, v])
pack = []
for i in range(n+1):
    pack.append([])
    for c in range(k+1):
        if i==0 or c==0:
            pack[i].append(0)
        elif cargo[i-1][0] <= c:
            pack[i].append(
                max(cargo[i-1][1]+pack[i-1][c-cargo[i-1][0]],pack[i-1][c])
                           )
        else:
            pack[i].append(pack[i-1][c])
print(pack[n][k])