exp = input()
minus_arr = exp.split('-')
for i, s in enumerate(minus_arr):
    plus_sum = 0
    for dig in s.split('+'):
        plus_sum += int(dig)
    minus_arr[i] = plus_sum

result = minus_arr[0]
for i in range(1,len(minus_arr)):
    result -= minus_arr[i]
print(result)