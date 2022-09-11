import collections
import heapq
import sys

n = int(sys.stdin.readline())
answer = []
for _ in range(n):
    tn, fn = map(int,sys.stdin.readline().split())
    l = list(map(int,sys.stdin.readline().split()))
    que = collections.deque()
    heap = []
    result = 0

    for i, ele in enumerate(l):
        que.append((i,ele))
        heapq.heappush(heap,-ele)
    max = -heapq.heappop(heap)
    while True:
        popleft = que.popleft()
        if popleft[1]==max:
            result +=1
            if popleft[0] == fn:
                break
            else:
                max = -heapq.heappop(heap)
        else:
            que.append(popleft)

    answer.append(result)
for ele in answer:
    print(ele)