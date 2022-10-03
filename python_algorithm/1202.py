# bag를 무게의 오름 차순 순서로 정렬
# jw 를 무게의 오름 차순 순서로 정렬
# 각 bag 에 대해서 들어갈 수 있는 jw 를 모두 heap 에 넣어줌 (-jw[1],jw[0],
#
import heapq
import sys

N, K  = map(int,sys.stdin.readline().split())
jw = []
for _ in range(N):
    heapq.heappush(jw, list(map(int, sys.stdin.readline().split())))
tv = 0
bag = [int(sys.stdin.readline()) for _ in range(K)]
bag.sort()
heap = []
for b in bag:
    while jw and jw[0][0] <= b:
        heapq.heappush(heap,-heapq.heappop(jw)[1])
    if heap:
        tv -= heapq.heappop(heap)
    elif not jw:
        break
print(tv)