import collections
import sys


# 동전이 떨어지는 경우
def is_out(y: int, x: int):
    if y < 0 or y >= vertical or x < 0 or x >= horizontal:
        return True
    return False


# 동전이 벽에 부딪힌 경우
def is_wall(y: int, x: int):
    if graph[y][x] == '#':
        return True
    return False


def bfs():
    que = collections.deque([(coins[0], coins[1], 0)])
    visited = set()
    visited.add(tuple(coins))
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while que:
        coin1, coin2, number_of_try = que.popleft()
        if number_of_try > 10:
            return -1
        for dy, dx in direction:
            cy1, cx1 = coin1[0] + dy, coin1[1] + dx
            cy2, cx2 = coin2[0] + dy, coin2[1] + dx
            # 둘 다 아웃인 경우
            if is_out(cy1, cx1) and is_out(cy2, cx2):
                continue
            # coin1 만 아웃인 경우 혹은 coin2 만 아웃인 경우
            elif is_out(cy1, cx1) or is_out(cy2, cx2):
                return number_of_try + 1
            # 둘 다 아웃이 아닌 경우
            else:
                # 둘 모두 벽에 부딪힌 경우
                if is_wall(cy1, cx1) and is_wall(cy2, cx2):
                    continue
                # coin1 이 벽에 부딪힌 경우
                elif is_wall(cy1, cx1):
                    if ((coin1[0], coin1[1]), (cy2, cx2)) not in visited and (
                            (cy2, cx2), (coin1[0], coin1[1])) not in visited:
                        if cy2 == coin1[0] and cx2 == coin1[1]:
                            continue
                        que.append(((coin1[0], coin1[1]), (cy2, cx2), number_of_try + 1))
                        visited.add(((coin1[0], coin1[1]), (cy2, cx2)))
                # coin2 이 벽에 부딪힌 경우
                elif is_wall(cy2, cx2):
                    if ((cy1, cx1), (coin2[0], coin2[1])) not in visited and (
                            (coin2[0], coin2[1]), (cy1, cx1)) not in visited:
                        if cy1 == coin2[0] and cx1 == coin2[1]:
                            continue
                        que.append(((cy1, cx1), (coin2[0], coin2[1]), number_of_try + 1))
                        visited.add(((cy1, cx1), (coin2[0], coin2[1])))
                # 둘 모두 벽에 부딪히지 않았을 경우
                else:
                    if ((cy1, cx1), (cy2, cx2)) not in visited and ((cy2, cx2), (cy1, cx1)) not in visited:
                        que.append(((cy1, cx1), (cy2, cx2), number_of_try + 1))
                        visited.add(((cy1, cx1), (cy2, cx2)))
    return -1


vertical, horizontal = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(vertical)]
coins = []

for i in range(vertical):
    for j in range(horizontal):
        if graph[i][j] == 'o':
            coins.append((i, j))
answer = bfs()
# 10 번째에서 11뻔째로 넘어갈 때 답이 나오는 경우 11이 출력될 수도 있다.
if answer > 10:
    print(-1)
else:
    print(answer)
