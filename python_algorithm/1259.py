import sys

answer = []
while(1):
    word= sys.stdin.readline().rstrip()
    if word == '0':
        break
    if word == word[::-1]:
        answer.append('yes')
    else:
        answer.append('no')
for a in answer:
    print(a)
