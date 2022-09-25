import sys

N, M = map(int,sys.stdin.readline().split())
not_seen = set()
answer = []
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    not_seen.add(name)
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    if name in not_seen:
        answer.append(name)
print(len(answer))
for n in sorted(answer):
    print(n)