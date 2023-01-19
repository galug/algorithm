# 이상한 소수
# 왼쪽 부터 n 자리 까지 모두 소수인 수를 이상한 소수라고 하고 이상한 소수를 모두 구한다.
import math
# 소수인지 판별하는 함수
def is_prime(number: int):
    sqrt = int(math.sqrt(number))
    # sqrt + 1 까지의 수까지 나눠지지 않으면 소수
    for i in range(2, sqrt + 2):
        if number % i == 0:
            return False
    return True

# 자리수를 입력
n = int(input())
# 자리수에 맞는 범위를 지정
MAX = 1
for _ in range(n):
    MAX *= 10
MIN = MAX // 10
# 이상한 소수를 담는 prime
prime = [[]]
prime.append([2, 3, 5, 7])
# n 자리수의 이상한 소수를 구하는 반복문
for p_idx in range(2, n + 1):
    prime.append([])
    # 1. n 자리 이상한 소수를 구하기 위해서는 n - 1 자리의 이상한 소수의 맨 뒤자리에 숫자를 추가
    # 2. 소수 여부 확인
    for amazing_prime in prime[p_idx - 1]:
        for can_amazing_prime in range(amazing_prime * 10 + 1, amazing_prime * 10 + 10):
            if is_prime(can_amazing_prime):
                prime[p_idx].append(can_amazing_prime)
for a in prime[n]:
    print(a)
# for p in range(2, MAX):
#     is_not_amazing = False
#     temp_p = p // 10
#     if is_prime(p):
#         prime.append(p)
#     else:
#         continue
#     while temp_p > 0:
#         if temp_p not in prime:
#             is_not_amazing = True
#             break
#         temp_p //= 10
#     if is_not_amazing:
#         continue
#     if MIN <= p < MAX:
#         answer.append(p)
for a in answer:
    print(a)
