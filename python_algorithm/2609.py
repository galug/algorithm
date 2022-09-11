import sys

n, m = map(int,sys.stdin.readline().split())
a = min(n,m)
b = max(n,m)

while a!=0:
    b, a = a, b%a
print(b)
print(b*(n//b)*(m//b))