# dp 문제
# 최소 값을 낼 수 있는 것들을 고른다.
# 다시 풀어 봅시다.
import collections
import sys

total_days = int(input())
dp = [0] * (total_days + 1)
k = 0
# 핵심은 과거에 일을 받아서 미래 시점까지 일을 하면 현재시점에 일을 받아서 미래 시점까지 일을 하는 것 중 하나만 가능하다는 점
for i in range(total_days):
    # 상담 요구 시간, 이득을 받는다.
    required_days, benefits = map(int, sys.stdin.readline().split())
    # 현재 날(i - 1) 까지 받은 수익의 최대값을 구한다. 어짜피 뒤의 날짜이기 때문에 갱신해야함
    k = max(k, dp[i])
    # 퇴사 날짜 지난 경우 continue
    if required_days + i > total_days:
        continue
    # i + required_days 에 이전 일을 해서 받은 돈 vs 현재까지 받은 돈 + 이 일을 할 시 받을 돈 비교
    dp[i + required_days] = max(dp[i + required_days], k + benefits)

print(max(dp))
'''
# 나의 풀이 
# 좀 느리다. 

total_days = int(input())
dp = [0] * total_days

for i in range(total_days):
    required_days, benefits = map(int, sys.stdin.readline().split())
    # graph[상담이 끝난 날].append((상담 시작일, benefits))
    graph[required_days + i - 1].append((i, benefits))

# dp = max(dp[상담끝난 날], dp[graph[상담 끝난 날] 중 시작일 - 1] +  benefits)
for i in range(total_days):
    for s, b in graph[i]:
        dp[i] = max(dp[i], dp[s - 1] + b)
    dp[i] = max(dp[i], dp[i-1])

print(dp[total_days-1])
'''
