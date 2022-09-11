n = int(input())

l = []
i = 0
curse = '666'
while(len(l)<n):
    if curse in str(i):
        l.append(i)
    i+=1
print(i-1)