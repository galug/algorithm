import sys

n =int(input())
se = 0
for _ in range(n):
    l = sys.stdin.readline().split()
    op = l[0]
    if len(l)==2:
        n = 1<<int(l[1])
    if op == 'add':
        se |= n
    if op == 'remove':
        se &= ~n
    if op == 'check':
        if n &se != 0:
            print(1)
        else:
            print(0)
    if op == 'toggle':
        se ^= n
    if op == 'all':
        se |= (1<<21) -1
    if op == 'empty':
        se = 0