# 클립보드 문제
# 4가지 동작을 이용해서 만들 수 있는 최댓 값 뽑기

# N번의 최댓값과 입력값 받기
MAX_INPUT = 101
n = int(input())

# 기본 최댓값들
dp = [0] * MAX_INPUT
dp[1] = 1
dp[2] = 2

# n 번째 까지의 최댓값을 상향식(tabulation) 방법으로 해결
for i in range(3, n + 1):
    # 화면에 A를 출력한다
    dp[i] = dp[i - 1] + 1
    # 클립 보드를 이용한 복붙 연산으로 출력값을 늘린다.
    for j in range(3, i):
        if dp[i] < dp[i - j] * (j - 1):
            dp[i] = dp[i - j] * (j - 1)

print(dp[n])
