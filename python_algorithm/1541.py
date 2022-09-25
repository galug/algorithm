
str = input()
op_list = str.split('-')

op_l = []
answer = 0
for str in op_list:
    if '+' in str:
        plust_list = str.split('+')
        temp = 0
        for p in plust_list:
            temp += int(p)
        op_l.append(temp)
    else:
        op_l.append(int(str))
answer += op_l[0]
for i in range(1,len(op_l)):
    answer-= op_l[i]
print(answer)