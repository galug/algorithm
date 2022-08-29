import collections

dp = collections.defaultdict()
def fib_1(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp [i - 2]
    return dp[n]
def fib_2(n):
    if n<= 1:
        return n
    if dp[n]:
        return dp[n]
    dp[n] = fib_2(n-1) + fib_2(n-2)
    return dp[n]
print(fib_1(5))