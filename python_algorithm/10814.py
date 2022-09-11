import sys

n = int(input())
l = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    l.append((int(age),name))
l.sort(key=lambda x : x[0])
for ele in l:
    print(ele[0], ele[1])
