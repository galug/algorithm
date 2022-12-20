# src -> dest 로 향하는 최소 연산 개수를 세준다.
import collections
import sys

src, destination = map(int, sys.stdin.readline().split())
visited = set()


# bfs 를 통한 풀이
def bfs():
    que = collections.deque([src])
    count = 0
    # 한 번의 과정이 끝날 때마다 count를 올려준다.
    while que:
        que_length = len(que)
        count += 1
        # 하나의 연산 cycle
        for _ in range(que_length):
            change_number = que.popleft()
            if change_number == destination:
                return count
            if change_number not in visited:
                if change_number * 2 <= destination:
                    que.append(change_number * 2)
                if change_number * 10 + 1 <= destination:
                    que.append(change_number * 10 + 1)
                visited.add(change_number)
    return -1


def calculate(end_number: int, start_number: int):
    count = 1
    while True:
        if end_number == start_number:
            return count
        if end_number > start_number:
            return -1
        if start_number % 10 == 1:
            start_number = (start_number-1) // 10
            count += 1
        elif start_number % 2 == 0:
            start_number /= 2
            count += 1
        else:
            return -1



print(calculate(src, destination))
