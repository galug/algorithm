# 병사의 뭉쳐 있는 정도를 계산하는 식
import collections
import sys
# 그래프의 가로, 세로와 그래프를 입력받는다.
horizontal, vertical = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(vertical)]
# 들른 곳을 표현하기 위한 변수이다.
visited = [[0] * horizontal for _ in range(vertical)]


# 동맹인지 아닌지 확인
def is_ally(y, x, color):
    if 0 <= y < vertical and 0 <= x < horizontal and graph[y][x] == color:
        return True
    return False

# 넓이 우선 탐색으로 개수를 센다.
def bfs(y, x, color):
    count = 1
    graph[y][x] = 1
    que = collections.deque([[y, x]])

    direct_x = [0, 0, -1, 1]
    direct_y = [1, -1, 0, 0]

    while que:
        y, x = que.popleft()
        for direct_index in range(4):
            move_x = direct_x[direct_index]
            move_y = direct_y[direct_index]
            if is_ally(y + move_y, x + move_x, color) and visited[y + move_y][x + move_x] == 0:
                visited[y + move_y][x + move_x] = 1
                que.append([y+move_y, x+move_x])
                count += 1
    return count


black_count = 0
white_count = 0

for i in range(vertical):
    for j in range(horizontal):
        if graph[i][j] == 'W' and visited[i][j] == 0:
            temp_count = bfs(i, j, 'W')
            white_count += (temp_count*temp_count)
        if graph[i][j] == 'B' and visited[i][j] == 0:
            temp_count = bfs(i, j, 'B')
            black_count += (temp_count*temp_count)

print(white_count, black_count)
