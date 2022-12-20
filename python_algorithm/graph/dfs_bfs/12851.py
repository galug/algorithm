# 원하는 숫자로 몇 번의 연산까지 갈 수 있고 그 때의 방법의 숫자
# 더 좋은 풀이 있나 찾아보자 !
import sys
import collections

src, destination = map(int, sys.stdin.readline().split())
# bfs 를 통한 풀이
que = collections.deque([src])
count = -1
number_of_ways = 0
dp_count = [0] * (100_000 + 1)
# 한 번의 과정이 끝날 때마다 count 를 올려준다.
while que:
    que_length = len(que)
    count += 1
    # 하나의 연산 cycle
    for _ in range(que_length):
        change_number = que.popleft()
        if dp_count[change_number] == 0 or dp_count[change_number] == count:
            dp_count[change_number] = count
            if change_number == destination:
                number_of_ways += 1
            elif change_number > destination:
                que.append(change_number - 1)
            else:
                if change_number * 2 <= 100_000:
                    que.append(change_number * 2)
                if change_number + 1 <= 100_000:
                    que.append(change_number + 1)
                if change_number - 1 >= 0:
                    que.append(change_number - 1)
    if number_of_ways != 0:
        break
print(count)
print(number_of_ways)
