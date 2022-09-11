import sys

N, r, c = map(int,sys.stdin.readline().split())
max_side = 2**(N-1)
answer = 0
block = 4**(N-1)
while block > 0:
    if r >= max_side:
        if c >= max_side:
            answer += (block * 3)
            r -= max_side
            c -= max_side
        else:
            answer += (block * 2)
            r -= max_side
    else:
        if c >= max_side:
            c-= max_side
            answer += block

    block = block // 4
    max_side = max_side // 2
print(answer)