n = int(input())

max_g = n//5

for i in range(max_g,-1,-1):
    if (n-5*i)%3==0:
       print(i+(n-i*5)//3)
       exit(0)
print(-1)