# 뿌요뿌요 구현
import collections
import sys

# 같은 puyo 를 지닌 graph 인지 판단
def is_same(y, x, block):
    if 0 <= x < 6 and 0 <= y < graph_height[x] and graph[x][y] == block:
        return True
    return False

# 뿌요를 터뜨릴 수 있는지 판단하고 터뜨릴 수 있을 시
def bfs(y, x, block, broken):
    count = 1
    blocks = collections.defaultdict(list)
    blocks[x].append(y)
    # 터뜨릴 수 있는 뿌요를 que 에 추가
    que = collections.deque([(y, x)])
    while que:
        _y, _x = que.popleft()
        for dy, dx in direction:
            if dy + _y not in blocks[dx + _x]:
                if is_same(dy + _y, dx + _x, block):
                    count += 1
                    que.append((dy + _y, dx + _x))
                    blocks[dx + _x].append(dy + _y)
    # 터뜨릴수 있는 뿌요들을 broken 에 저장한다.
    if count >= 4:
        for bx in range(6):
            for by in blocks[bx]:
                broken.append([bx, by])


# . 을 제외한 맵의 생김새와 각각의 x 좌표에서의 길이를 구한다.
graph = [[] for _ in range(6)]
graph_height = [0] * 6
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0
# 공백을 제외한 뿌요들을 입력받는다.
for _ in range(12):
    line = list(map(str, sys.stdin.readline().rstrip()))
    for idx_x in range(6):
        if line[idx_x] != '.':
            graph[idx_x].append(line[idx_x])
            graph_height[idx_x] += 1
# 뿌요를 아래에서 위로 향하게끔한다.
for reverse_x in range(6):
    graph[reverse_x].reverse()
# 더 이상 뿌요가 터지지 않을 때까지 반복한다.
while True:
    has_not_puyo = True
    broken_puyo = []
    # 이번 회차에 터질 뿌요들을 저장한다.
    for _x in range(6):
        for _y in range(len(graph[_x])):
            if [_x, _y] not in broken_puyo:
                bfs(_y, _x, graph[_x][_y], broken_puyo)
    # 터진 뿌요가 존재하지 않는다면 반복을 그만한다.
    if not broken_puyo:
        break
    # 이번 회차에 터진 뿌요들을 없애준다.
    broken_puyo.sort(key=lambda x: -x[1])
    for x, y in broken_puyo:
        graph[x].pop(y)
    for x in range(6):
        graph_height[x] = len(graph[x])
    answer += 1

print(answer)
