ch = int(input())
brk_n = int(input())
brk_btn = list()
if brk_n!=0:
    brk_btn = input().split()
min_cnt = abs(100-ch)

for i in range(500000):
    if i > min_cnt:
        break
    pcheck = True
    mcheck = True
    if brk_btn:
        if ch-i>=0:
            for btn in brk_btn:
                if btn in str(ch - i):
                    mcheck = False
                    break
        else:
            mcheck = False
        for btn in brk_btn:
            if btn in str(ch + i):
                pcheck = False
                break
    if mcheck:
        min_cnt = min(min_cnt, i + len(str(ch - i)))
        break
    if pcheck:
        min_cnt = min(min_cnt, i + len(str(ch+i)))
        break
print(min_cnt)