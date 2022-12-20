import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())

# set로 받는 이유는 같은 coin이 들어올 수 있기 때문
coins = list(i for i in set(int(read()) for _ in range(n)) if i <= k)

if k in coins:
    print(1)
    exit()

que = deque((i, coin) for i, coin in enumerate(coins))
visit = [0] * (k + 1)

for i in coins:
    visit[i] = 1

cnt = 1
while que:
    for _ in range(len(que)):
        index, coin_sum = que.popleft()

        for i in range(index, len(coins)):
            new_sum = coin_sum + coins[i]
            if new_sum == k:
                print(cnt + 1)
                exit(0)
            if new_sum <= k and not visit[new_sum]:
                que.append((i, new_sum))
                visit[new_sum] = 1
    cnt += 1

print(-1)
