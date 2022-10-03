import sys

N = int(input())
positions = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer = 0
positions.append(positions[0])
tf = 0
ts = 0
for i in range(N):
    tf += positions[i][0]*positions[i+1][1]
    ts += positions[i][1]*positions[i+1][0]
print(round((abs(tf-ts)/2),1))