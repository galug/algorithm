import collections
import heapq
import sys

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    answer =[]
    dict = collections.defaultdict(int)
    for _ in range(n):
        op, n = sys.stdin.readline().split()
        if op == 'I':
            n = int(n)
            heapq.heappush(max_heap,-n)
            heapq.heappush(min_heap,n)
            dict[n] += 1
        elif n == '1':
            while max_heap:
                max_num = heapq.heappop(max_heap) * -1
                if max_num in dict and dict[max_num] != 0:
                    dict[max_num] -= 1
                    break
        else:
            while min_heap:
                min_num = heapq.heappop(min_heap)
                if min_num in dict and dict[min_num] != 0:
                    dict[min_num] -= 1
                    break
    while max_heap:
        m = heapq.heappop(max_heap) * -1
        if m in dict and dict[m] != 0:
            answer.append(m)
            break
    while min_heap:
        m = heapq.heappop(min_heap)
        if m in dict and dict[m] != 0:
            answer.append(m)
            break
    if len(answer) == 0:
        print('EMPTY')
    elif len(answer) == 1:
        print(answer[0], answer[0])
    else:
        print(answer[0], answer[1])
