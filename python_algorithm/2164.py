import collections

n = int(input())
# que 를 이용한 정직한 방법
# j= 0
# deque = collections.deque()
# for i in range(1,n+1):
#     deque.append(i)
# while len(deque)>1:
#     if j %2 == 0:
#         deque.popleft()
#     else:
#         popleft = deque.popleft()
#         deque.append(popleft)
#     j+=1
# print(deque.pop())
i=1
while i<n:
    i*=2
if i==n:
    print(i)
else:
    i = i//2
    print((n%i)*2)