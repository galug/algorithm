import collections
import sys


# 미네랄이 있는지확인하는 함수
def is_mineral(y, x):
    if 0 <= y < vertical and 0 <= x < horizontal and graph[y][x] == 'x':
        return True
    return False


# 공중에 떠있는지 확인하는 함수
def is_floating(y, x, visit):
    # 애초에 바닦이므로 떠있지 않음
    if y == 0:
        return False
    que = collections.deque([(y, x)])
    visit[x].append(y)
    # 클러스의 모든 부분을 추적
    while que:
        my, mx = que.popleft()
        # 바닥에 닿아 있으면 떠있지 않음
        if my == 0:
            return False
        for fy, fx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            # 방문한 적이 없고 미네랄이 있으면 큐에 넣고 방문한 곳으로 추가
            if (my + fy not in visit[mx + fx]) and is_mineral(my + fy, mx + fx):
                que.append((my + fy, mx + fx))
                visit[mx + fx].append(my + fy)
    # 바닦에 닿아있는 부분이 없으므로 떠있다
    return True


# 아래에 떨구는 함수
def drop(visit):
    # 얼마나 떨구는지 계산하는 부분
    drop_height = 101
    for _x in visit:
        if visit[_x]:
            drop_height = min(drop_height, min(visit[_x]))
            for _y in visit[_x]:
                if _y - 1 in visit[_x]:
                    continue
                for below_h in range(_y - 1, -1, -1):
                    if below_h in visit[_x]:
                        break
                    if graph[below_h][_x] == 'x':
                        drop_height = min(drop_height, _y - below_h - 1)
                        continue
    # 기존 클러스터를 모두 지워줌
    for _x in visit:
        for _y in visit[_x]:
            graph[_y][_x] = '.'
    # 내려간 높이만큼 클러스터를 다시 그려줌
    for _x in visit:
        for _y in visit[_x]:
            graph[_y - drop_height][_x] = 'x'


# 그래프 그리기
def draw_graph():
    graph.reverse()
    for y in range(vertical):
        for x in range(horizontal):
            print(graph[y][x], end='')
        if y != vertical - 1:
            print()


vertical, horizontal = map(int, sys.stdin.readline().split())

# 맵의 입력을 받고 계산의 편의를 위해 뒤집어 준다.
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(vertical)]
graph.reverse()

throw_number = int(input())
throw_heights = list(map(int, sys.stdin.readline().split()))

# 던진 창들을 모두 조사해준다.
for order_idx, h in enumerate(throw_heights):
    h -= 1
    # 홀수 번째에는 왼쪽에서 창을 던진다.
    if order_idx % 2 == 0:
        for left_idx in range(horizontal):
            if graph[h][left_idx] == 'x':
                graph[h][left_idx] = '.'
                for dy, dx in ((0, 1), (1, 0), (-1, 0)):
                    visited = collections.defaultdict(list)
                    if is_mineral(h + dy, left_idx + dx) and is_floating(h + dy, left_idx + dx, visited):
                        drop(visited)
                        break
                break
    # 짝수 번째에는 오른쪽에서 창을 던진다.
    else:
        for right_idx in range(horizontal - 1, -1, -1):
            if graph[h][right_idx] == 'x':
                graph[h][right_idx] = '.'
                for dy, dx in ((0, -1), (1, 0), (-1, 0)):
                    visited = collections.defaultdict(list)
                    if is_mineral(h + dy, right_idx + dx) and is_floating(h + dy, right_idx + dx, visited):
                        drop(visited)
                        break
                break
# 그래프를 다시 뒤집고 그려준다.
draw_graph()
