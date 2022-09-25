import math
import sys

n, m = map(int,sys.stdin.readline().split())

print((math.factorial(n) // math.factorial(n-m))//math.factorial(m))