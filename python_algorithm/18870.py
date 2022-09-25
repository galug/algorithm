import collections
import sys

n = int(input())
line = list(map(int,sys.stdin.readline().split()))
answer = []

sorted_st = list(set(line[::]))
sorted_st.sort()
dict = collections.defaultdict(int)
for i, num in enumerate(sorted_st):
    dict[num] = i
for ele in line:
    print(dict[ele], end =' ')
