import sys

N = int(input())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
zero = sys.maxsize
answer = [0,0,0]
for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        temp = l[i] +l[left]+l[right]
        if abs(temp) < zero:
            zero = abs(temp)
            answer[0],answer[1],answer[2] = l[i],l[left], l[right]
        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        else:
            print(l[i], l[left],l[right])
            sys.exit(0)
print(answer[0],answer[1],answer[2])