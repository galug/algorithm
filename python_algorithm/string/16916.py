import sys

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

answer = 0

pi_table = [0]* len(p)

def get_pi():
    for i in range(1, len(p)):
        for j in range(i//2 + 1):
            if p[:j] == p[i-j:i]:
                pi_table[i] = j

get_pi()

print(pi_table)
