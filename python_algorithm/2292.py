# 정직한 풀이
# n = int(input())
# i = 0
# min_num = 1
# if n==1:
#     print(1)
# else:
#     while 1:
#         if min_num <= n and n < min_num + i * 6:
#             print(i+1)
#             break
#         i += 1
#         if i == 1:
#             min_num += i
#         else:
#             min_num += ((i - 1) * 6)

# 규칙성을 찾고 점화식을 이용한 해 
def f(n):
    result=1
    k=1
    while 1:
        result=3*k*(k-1)+1
        if result>=n:
            return k
        k+=1
a=int(input())
print(f(a))