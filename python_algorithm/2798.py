import sys

n , m = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
max_sum = 0
l.sort()
for i in range(n-2):
    low = i+1
    high = n-1
    while low<high:
        temp = l[i] + l[low] + l[high]
        if temp < m:
            max_sum = max(max_sum, temp)
            low += 1
        elif temp > m:
            high -= 1
        else:
            print(m)
            sys.exit(0)
print(max_sum)