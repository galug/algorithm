import sys

n = int(input())
it = list(map(int, sys.stdin.readline().split()))
dp = [it[0]]
for i in range(1,len(it)):
    if dp[-1] < it[i]:
        dp.append(it[i])
    else:
        temp = it[i]
        lower, high = 0, len(dp) - 1
        while lower <= high:
            mid = lower +high
            if dp[mid] == temp:
                break
            if dp[mid] < temp:
                lower = mid + 1
            else:
                high = mid - 1
        if not dp[mid] == temp:
            dp[lower] = temp
print(len(dp))