import sys

n = int(sys.stdin.readline())

temp = []
answer = []
suc = True
count = 1
temp = []
for i in range(n):
    k = int(sys.stdin.readline())
    while count <= k:
        temp.append(count)
        answer.append('+')
        count += 1
    if k == temp[-1]:
        temp.pop()
        answer.append('-')
    else:
        suc = False

if suc == False:
    print('NO')
else:
    for e in answer:
        print(e)
