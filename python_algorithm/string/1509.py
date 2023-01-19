# 팰린 드롬 + DP
import sys

request = sys.stdin.readline().rstrip()
length = len(request)

# 모든 팰린드롬을 구해준다.
odd = []
even = []
for i in range(length - 1):
    if i == 0:
        if request[i] == request[i + 1]:
            even.append((i, i + 1))
        continue
    if request[i] == request[i + 1]:
        even.append((i, i + 1))
    if request[i - 1] == request[i + 1]:
        odd.append((i - 1, i + 1))
while True:
    new_even = []
    for start, end in even:
        new_start, new_end = start - 1, end + 1
        if new_start >= 0 and new_end < length and request[new_start] == request[new_end]:
            new_even.append((new_start, new_end))
    if not new_even:
        break
    even = new_even

while True:
    new_odd = []
    for start, end in odd:
        new_start, new_end = start - 1, end + 1
        if new_start >= 0 and new_end < length and request[new_start] == request[new_end]:
            new_odd.append((new_start, new_end))
    if not new_odd:
        break
    odd = new_odd

all_palindrom = even + odd
all_palindrom.sort()
print(all_palindrom)
# 팰린드롬 중에서
dp = [0] * len(all_palindrom)