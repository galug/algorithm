# n 을 만들 수 있는 숫자들의 합 중 가장 많은 숫자를 고른다.
# 기본 골자: 1 ~ i 까지의 합이 n 과 일치할 경우 최대 개수가 된다. 1~i-1 까지의 합 < n < 1~i 까지의 합
# i - 1이 답이 된다.

n = int(input())

i = 1
total = 0
while True:
    total += i
    if total > n:
        break
    i += 1

print(i - 1)