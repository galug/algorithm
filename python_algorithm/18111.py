import collections
import sys

N, M , B = map(int,sys.stdin.readline().split())
grounds = []
for _ in range(N): grounds += list(map(int,sys.stdin.readline().split()))
answer = sys.maxsize
sum_block = sum(grounds) + B
grounds = collections.Counter(grounds)
low = min(grounds)
high = max(grounds)
idx = 0
for i in range(low, high+1):
    total = 0
    if sum_block >= i*N*M:
        for ele, c in grounds.items():
            if i > ele:
                temp = i - ele
                total += temp * c
            else:
                temp = ele - i
                total += temp * 2 * c
        if total <= answer:
            answer = total
            idx = i
print(answer, idx)