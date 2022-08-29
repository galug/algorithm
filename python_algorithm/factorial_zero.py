N = int(input())
five_pow = [0,0,0]
five_pow[0] = N//5
five_pow[1] = N//25
five_pow[2] = N//125
result = 0
for i in range(len(five_pow)):
    result += five_pow[i]
print(result)