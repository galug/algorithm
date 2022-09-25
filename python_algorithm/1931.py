import sys

n = int(input())
lecture = []
for _ in range(n):
    start, end = map(int,sys.stdin.readline().split())
    lecture.append([start,end])
lecture.sort(key= lambda x: (x[1],x[0]))
answer = 0
last = 0
for i,l in enumerate(lecture):
    if l[0] >= last:
        answer+=1
        last = l[1]
print(answer)