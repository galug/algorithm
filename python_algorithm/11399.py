import sys

n = int(input())
line = list(map(int,sys.stdin.readline().split()))
line.sort()
for i in range(len(line)):
    if i==0:
        continue
    line[i] += line[i-1]
print(sum(line))