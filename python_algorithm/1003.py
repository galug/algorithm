import sys

t = int(input())
answer = [[1,0],[0,1]]
q = [int(sys.stdin.readline()) for _ in range(t)]
max_q = max(q)
for i in range(2,max_q+1):
    answer.append([answer[i-2][0]+answer[i-1][0], answer[i-2][1]+answer[i-1][1]])
for ele in q:
    print(answer[ele][0],answer[ele][1])
