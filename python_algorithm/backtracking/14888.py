import sys

n = int(input())
number_list = list(map(int, sys.stdin.readline().split()))
operation = list(map(int, sys.stdin.readline().split()))

max_sum = [-sys.maxsize]
min_sum = [sys.maxsize]


def dfs(i, s):
    if i == n:
        min_sum[0] = min(min_sum[0], s)
        max_sum[0] = max(max_sum[0], s)
        return
    if operation[0] > 0:
        operation[0] -= 1
        dfs(i + 1, s + number_list[i])
        operation[0] += 1
    if operation[1] > 0:
        operation[1] -= 1
        dfs(i + 1, s - number_list[i])
        operation[1] += 1
    if operation[2] > 0:
        operation[2] -= 1
        dfs(i + 1, s * number_list[i])
        operation[2] += 1
    if operation[3] > 0:
        operation[3] -= 1
        if s < 0:
            dfs(i + 1, -((-s) // number_list[i]))
        else:
            dfs(i + 1, s // number_list[i])
        operation[3] += 1


dfs(1, number_list[0])

print(max_sum[0])
print(min_sum[0])
