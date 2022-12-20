# 그래프 중 붙어 있는 부분을 하나의 단지로 보고
# 그 단지들을 이루는 아파트 개수를 오름 차순으로 정렬한다.
import collections
import sys

# 그래프와 그래프의 변 길이 입력받기
n = int(input())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
answer = []


# 아파트가 그래프의 지정 부분에 존재하는지 확인하는 함수
def in_graph(i, j):
    if 0 <= i < n and 0 <= j < n and graph[i][j] == 1:
        return True
    return False


# 지금 위치에서 사방을 모두 확인한다.
direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]


# 주어진 위치에 아파트가 속하는 단지의 아파트 개수를 구하는 함수이다.
def bfs(y, x):
    # 주어진 위치에는 아파트가 존재하므로 que에 추가하고 아파트 존재를 지운다.
    que = collections.deque([[y, x]])
    graph[y][x] = 0
    # 단지 내 아파트 개수
    count = 0
    # 아파트의 위치를 계속해서 뽑아낸다.
    while que:
        y, x = que.popleft()
        count += 1
        # 4방향 탐색
        for direct_index in range(4):
            move_x = direction_x[direct_index]
            move_y = direction_y[direct_index]
            # 주어진 방향에 아파트가 존재할시 단지 내 아파트 que에 추가함과 동시에 아파트 존재를 삭제
            if in_graph(y + move_y, x + move_x):
                graph[y + move_y][x + move_x] = 0
                que.append([y + move_y, x + move_x])
    return count


for i in range(n):
    for j in range(n):
        # 그래프에서 아파트가 발견되는 위치를 기준으로 단지의 개수를 찾아본다.
        if graph[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()

for c in answer:
    print(c)
