# 달리기 문제
# 한 번에 여러 개의 줄을 갈 수 있을 때 도착 지점까지 도달하는 최소 방법
import collections
import sys
# 문제 입력 받기
vertical, horizontal, move_distance = map(int, sys.stdin.readline().split())

graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(vertical)]

y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
# 좌표 배열에서 쓸 수 있게 변경
x1, y1 = x1 - 1, y1 - 1
x2, y2 = x2 - 1, y2 - 1

# 방문한 곳이 몇 번의 이동으로 도착하였는지 확인한다.
visited_graph = [[0] * horizontal for _ in range(vertical)]

# 너비 우선 탐색을 통한 해결
def bfs():
    que = collections.deque([(y1, x1)])
    while que:
        y, x = que.popleft()
        # 네 방향으로 이동
        for move_y, move_x in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            # 주어진 이동 가능한 거리만큼 이동한다.
            for i in range(1, move_distance + 1):
                ny = y + move_y * i
                nx = x + move_x * i
                # 원하는 곳에 도착 시 에 빠져 나온다.
                if ny == y2 and nx == x2:
                    return visited_graph[y][x] + 1
                # 벽을 만나거나 마지막 길로 맵의 끝자락에 닿으면 그만 탐색
                if ny < 0 or ny >= vertical or nx < 0 or nx >= horizontal or graph[ny][nx] != '.':
                    break
                # if - elif 문에서 잘 못하여서 답이 제대로 나오지 않았다.
                # 아직 방문하지 않은 노드거나 현재 방문이 이전에 방문한 시간보다 짧은 시간일 경우 que 에 넣고 visited 를 갱신한다.
                if can_move(ny, nx, visited_graph[y][x] + 1):
                    que.append((ny, nx))
                    visited_graph[ny][nx] = visited_graph[y][x] + 1
                # 방문한 적이 있으며 현재 방문한 시간보다 짧을 시 que 에서 이미 탐색을 마쳤거나 앞으로 탐색할 예정이므로 빠져나온다.
                elif visited_graph[ny][nx] <= visited_graph[y][x]:
                    break
    return -1


def can_move(my: int, mx: int, moved_distance: int) -> bool:
    if visited_graph[my][mx] == 0 or visited_graph[my][mx] > moved_distance:
        return True
    return False


print(bfs())
