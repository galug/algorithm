n = int(input())
req = []
for _ in range(n):
    req.append(int(input()))
dn = {1:1, 2:2, 3:4}
m = max(req)
for i in range(4, m+1):
    dn[i] = dn[i-1]+dn[i-2] +dn[i-3]
for ans in req:
    print(dn[ans])