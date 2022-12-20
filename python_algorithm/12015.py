import sys

def binary_search(low, high, search : int):
    while low <= high:
        mid = (low +high)//2
        if dp[mid] >=search:
            high = mid - 1
        else:
            low = mid + 1
    return low
n = int(input())
na = list(map(int,sys.stdin.readline().split()))
dp = [na[0]]
dp_size = 1
for i in range(1,n):
    if dp[-1] <na[i]:
        dp.append(na[i])
        dp_size += 1
    else:
        dp[binary_search(0,dp_size-1,na[i])] = na[i]
print(dp_size)