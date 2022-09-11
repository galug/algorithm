n = int(input())
digit_num = len(str(n))
answer = 0
start = n - digit_num * 9
if start<1:
    start = 1
for i in range(start, n):
    str_n = str(i)
    result = i
    for k in str_n:
        result = result + int(k)
    if result == n:
        answer = i
        break
print(answer)
