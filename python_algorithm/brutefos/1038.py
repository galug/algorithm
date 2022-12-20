# n 번째 감소하는 수를 찾는 문제
import collections

n = int(input())

digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# que 를 이용해 풀어보자
que = collections.deque(digit)
count = -1

# que 에 decreased_number 을 계속 해서 추가하여준다.
while que and count <= 1_000_000:
    decreased_number = que.popleft()
    count += 1
    # 답이 나왔을 경우 빠져나온다.
    if count == n:
        print(decreased_number)
        break
    # 핵심로직
    # 자리수가 늘어난 최소 숫자를 자연스럽게 que 의 마지막에 추가함으로써 해결한다.
    mod = decreased_number % 10
    # 현재 자신의 숫자의 첫째 자리에 존재하는 숫자보다 작은 수를 끝에 추가한다.
    for i in range(mod):
        que.append(decreased_number * 10 + i)
# 이 부분은 솔직히 이해 안감
if n > 1022:
    print(-1)