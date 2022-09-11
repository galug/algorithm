import sys

n, m = map(int,sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
max_lan = sum(l)//len(l)
min_lan = 1
while min_lan<=max_lan:
    mid = (min_lan+max_lan)//2
    total_lan = 0
    for lan in l:
        total_lan += lan//mid
    if total_lan >= m:
        min_lan = mid+1
    else:
        max_lan = mid-1
print(max_lan)