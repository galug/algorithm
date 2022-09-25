n = int(input())

# dp = [1,2]
#
# for i in range(2,n):
#     dp.append(dp[i-2]+dp[i-1])
# print(dp[n-1]%10007)
x, y = 1, 2
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    for i in range(2, n):
        x, y = y, x + y
    print(y % 10007)