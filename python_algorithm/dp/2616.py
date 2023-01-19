# 세 수를 조합하여 가장 큰 수를 고를 수 있는 경우를 구하는 문제가 된다.
import collections
import sys
# 열차의 수와 열차에탄 사람의 수 한 화물차가 최대 끌고 갈 수 있는 열차의 수를 입력받는다.
number_of_carriages = int(input())
passengers = list(map(int, sys.stdin.readline().split()))
max_carriages = int(input())
# dp, left_dp, right_dp 를 받는다.
dp = []
left_dp = []
right_dp = []
# 화물차가 max_carriages 의 수만큼 끌고 갔을 때 실어서 갈 수 있는 사람의 수를 저장한다.
que = collections.deque()
number_of_passengers = 0
for p_idx, p in enumerate(passengers):
    if p_idx < max_carriages:
        que.append(p)
        number_of_passengers += p
        continue
    dp.append(number_of_passengers)
    # left_dp 에 한 대의 열차에서 맨 왼쪽에서 p_idx 까지 싫을 수 있는 최대 사람의 수를 저장한다.
    if len(left_dp) > 1:
        left_dp.append(max(left_dp[-1], number_of_passengers))
    else:
        left_dp.append(number_of_passengers)
    number_of_passengers -= que.popleft()
    number_of_passengers += p
    que.append(p)
dp.append(number_of_passengers)
left_dp.append(max(left_dp[-1], number_of_passengers))

# p_idx ~ 맨 오른쪽 열차 까지 1대의 화물차를 통해서 싫을 수 있는 최대 사람의 수를 저장한다.
right_dp.append(dp[-1])
for right_idx in range(len(dp) - 2, -1, -1):
    right_dp.append(max(right_dp[-1], dp[right_idx]))
right_dp.reverse()
answer = 0
# answer = 중앙 칸을 기준으로 왼쪽 오른쪽을 나눠서 더한다.
# 중앙 칸 기준으로 왼쪽 칸에서 태울 수 있는 최대 개수 + 중앙 칸 + 중앙 칸 기준으로 오른쪽 칸에서 태울수 있는 최대 개수
# 위 식을 바탕으로 중앙칸을 옮겨가면서 계산한다. 
for middle_idx in range(max_carriages, number_of_carriages - 2 * max_carriages):
    answer = max(answer, left_dp[middle_idx - max_carriages] + dp[middle_idx] + right_dp[middle_idx + max_carriages])

print(answer)