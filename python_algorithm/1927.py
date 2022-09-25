import heapq
import sys

x = int(input())
heap = []
answer = []
for _ in range(x):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap) == 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap,n)
for ele in answer:
    print(ele)