import sys
from bisect import bisect_left

n = int(input())
num_array = list(map(int,sys.stdin.readline().split()))
dp = [num_array[0]]
size_dp = 1
dp2 = [0]*n
top_i = 0
answer= []
for i, num in enumerate(num_array):
    if dp[-1] < num:
        dp.append(num)
        size_dp +=1
        dp2[i] = size_dp
        top_i = i
    else:
        bl = bisect_left(dp,num)
        dp[bl] = num
        dp2[i] = bl + 1
print(size_dp)
answer.append(num_array[top_i])
for i in range(top_i-1,-1,-1):
    if dp2[i] == size_dp - 1:
        size_dp-=1
        answer.append(num_array[i])
print(' '.join(str(answer[n]) for n in range(len(answer)-1,-1,-1)))