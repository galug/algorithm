# 원하는 숫자로 몇 번의 연산까지 갈 수 있고 그 때의 방법의 숫자
# 더 좋은 풀이 있나 찾아보자 !
# 내 실패 코드
import sys
import collections

src, destination = map(int, sys.stdin.readline().split())
# bfs 를 통한 풀이
dp = [0] * (100_000 + 1)
dist = [0] * 100001


def move(moving:int):
    answer = []
    for _ in range(dist[destination]):
        answer.append(moving)
        moving = dp[moving]
    answer.append(moving)
    print(' '.join(map(str, answer[::-1])))


def bfs():
    que = collections.deque([src])
    while que:
        change_number = que.popleft()
        if change_number == destination:
            print(dist[destination])
            move(destination)
            return
        for next_number in (change_number * 2, change_number + 1, change_number - 1):
            if 0 <= next_number <= 100_000 and dist[next_number] == 0:
                que.append(next_number)
                dp[next_number] = change_number
                dist[next_number] = dist[change_number] + 1


bfs()

''' 성공 코드 
def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()'''