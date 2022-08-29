n= int(input())
q = []
for _ in range(n):
    q.append(int(input()))
dyn = [[1,0],[0,1]]
for i in range(2,max(q)+1):
    dyn.append([dyn[i-2][0]+dyn[i-1][0],dyn[i-2][1]+dyn[i-1][1]])
for ele in q:
    print('{0} {1}'.format(dyn[ele][0],dyn[ele][1]))