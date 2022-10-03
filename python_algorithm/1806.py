import sys

N, S = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))

left = 0
result = 0
answer = sys.maxsize
for right in range(N):
    result += l[right]
    while result - l[left] >= S:
        result -= l[left]
        left += 1
    if result >= S and answer > right -left:
        answer = right - left + 1
if answer == sys.maxsize:
    print(0)
else:
    print(answer)