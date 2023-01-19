# 뮤탈리스크 문제
import collections
import sys
# scv 의 수
number_of_scv = int(input())
# scv 의 남은 체력수
hp_of_scv = list(map(int, sys.stdin.readline().split()))
# scv 의 수가 3보다 작다면 0인 scv를 포함시켜서 3개로 맞춰준다.
for _ in range(3 - len(hp_of_scv)):
    hp_of_scv.append(0)
# scv 의 체력을 저장할 공간
dp = collections.defaultdict()
dp[tuple(hp_of_scv)] = 0
# 공격받는 경우의 수
attacks = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [1, 9, 3], [1, 3, 9], [3, 1, 9]]
answer = 0
# 공격받았을 때의 경우의 수를 저장한다.
que = collections.deque([hp_of_scv])
while que:
    # 남은 체력들을 꺼낸다.
    hp1, hp2, hp3 = que.popleft()
    # 남은 체력들이 0보다 작으면 빠져나온다.
    if hp1 <= 0 and hp2 <= 0 and hp3 <= 0:
        answer = dp[(hp1, hp2, hp3)]
        break
    # 공격당한 경우의 수를 que 에 집어넣기
    for at1, at2, at3 in attacks:
        # 상향식 기록
        if (hp1 - at1, hp2 - at2, hp3 - at3) not in dp:
            que.append((hp1 - at1, hp2 - at2, hp3 - at3))
            dp[(hp1 - at1, hp2 - at2, hp3 - at3)] = dp[(hp1, hp2, hp3)] + 1
print(answer)
