import collections
import sys

n= int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
print(round(sum(l)/n))
print(l[len(l)//2])
counter =  collections.Counter(l).most_common(2)
if len(l)>1:
    if counter[0][1] == counter[1][1]:
        if counter[0][0] > counter[1][0]:
            print(counter[0][0])
        else:
            print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(l[0])
print(max(l)-min(l))
