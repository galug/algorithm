# 올바른 등식을 만들 수 있는 경우의 수
import collections
import sys

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
answer = numbers[-1]

number_count = {numbers[0]: 1}

for i in range(1, n - 1):
    new_number = numbers[i]
    new_number_count = {}
    for k, v in number_count.items():
        if k + new_number <= 20:
            if k + new_number in new_number_count:
                new_number_count[k + new_number] += v
            else:
                new_number_count[k + new_number] = v
        if k - new_number >= 0:
            if k - new_number in new_number_count:
                new_number_count[k - new_number] += v
            else:
                new_number_count[k - new_number] = v
    number_count = new_number_count
print(number_count[answer])