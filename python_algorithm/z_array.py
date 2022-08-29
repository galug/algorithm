import sys

N, r, c = map(int,sys.stdin.readline().split())
def recursive_square(n:int, row:int, column, start):
    if n == 1:
        return int(start + row*2 + column)
    half_length = (2**n) // 2
    if row <half_length and column < half_length:
        return recursive_square(n-1, row, column, start)
    elif row <half_length and column >= half_length:
        return recursive_square(n-1, row, column % 2, start + 2**half_length)
    elif row >= half_length and column < half_length:
        return recursive_square(n-1, row % 2, column, start + (2**half_length)*2)
    else:
        return recursive_square(n-1, row % 2, column %2, start + (2**half_length)*3)
print(recursive_square(N, r, c, 0))