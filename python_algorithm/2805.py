import collections
import sys

n, m = map(int,sys.stdin.readline().split())
trees = collections.Counter(map(int,sys.stdin.readline().split())).items()

low, high = 0, max(trees)[0]

while low <= high:
    mid = (low+high)//2
    temp = sum([(wood-mid)*c if wood>=mid else 0 for wood,c in trees])
    if temp >= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)