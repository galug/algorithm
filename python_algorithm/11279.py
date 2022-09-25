import heapq
import sys

n = int(input())
answer = []
heap = []
for _ in range(n):
    number= int(sys.stdin.readline())
    if number==0:
        if len(heap)== 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(heap)*-1)
    else:
        heapq.heappush(heap,number*-1)
for ele in answer:
    print(ele)