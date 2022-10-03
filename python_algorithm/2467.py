import sys

n = int(input())
l = list(map(int,sys.stdin.readline().split()))
l.sort()
left, right = 0, len(l) - 1
zero = sys.maxsize
zl = [0,1]
while left<right:
    temp = l[left] + l[right]
    if temp == 0:
        zl[0],zl[1] = left, right
        break
    elif temp > 0:
        if temp < zero:
            zero = temp
            zl[0], zl[1] = left, right
        right -=1
    else:
        if abs(temp) < zero:
            zero = abs(temp)
            zl[0], zl[1] = left, right
        left += 1
print(l[zl[0]],l[zl[1]])