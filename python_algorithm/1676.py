import sys

two_list = [0,0]
five_list = [0,0]

for i in range(2,int(sys.stdin.readline())+1):
    if i % 2 == 0:
        two_list.append(two_list[i//2]+1)
    else:
        two_list.append(0)
    if i % 5 == 0:
        five_list.append(five_list[i//5]+1)
    else:
        five_list.append(0)
print(min(sum(two_list),sum(five_list)))