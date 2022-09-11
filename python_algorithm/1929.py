import math
import sys

min_num, max_num = map(int,sys.stdin.readline().split())

not_prime = [False for _ in range(max_num + 1)]
not_prime[0] = True
not_prime[1] = True
for i in range(2,int(math.sqrt(max_num+1))+1):
    if not_prime[i]:
        continue
    for j in range(2*i,max_num+1,i):
        not_prime[j] = True
for i in range(min_num,max_num+1):
    if not not_prime[i]:
        print(i)