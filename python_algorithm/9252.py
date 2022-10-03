str1 = " " + input().rstrip()
str2 = " " + input().rstrip()
len_str1 = len(str1)
len_str2 = len(str2)
dp = [[0]*(len_str1) for _ in range(len_str2)]
answer = ""
for i in range(1,len_str2):
    for j in range(1,len_str1):
        if str1[j] == str2[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])
x = len_str1 - 1
y = len_str2 - 1
while x > 0 and y > 0:
    if dp[y][x-1] == dp[y][x]:
        x = x - 1
    elif dp[y-1][x] == dp[y][x]:
        y = y - 1
    else:
        answer += str2[y]
        x -= 1
        y -= 1
print(answer[::-1])