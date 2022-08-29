import sys

N = int(input())
M = int(input())
if M:
    br_btn = set(input().split())
else:
    br_btn = set()
abs_ch = abs(100 - N)
esc = False
for i in range(1000001):
    for j in range(len(str(N+i))+1):
        if j == len(str(N+i)):
            abs_ch = min(len(str(N + i)) + i, abs_ch)
            print(abs_ch)
            esc = True
            break
        if str(N+i)[j] in br_btn:
            break
    if esc:
        break
    for j in range(len(str(N-i))+1):
        if j == len(str(N-i)):
            abs_ch = min(len(str(N - i)) + i, abs_ch)
            print(abs_ch)
            esc = True
            break
        if str(N-i)[j] in br_btn:
            break
    if esc:
        break