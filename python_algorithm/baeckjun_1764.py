import sys

N, M = map(int, input().split())
dict_people = []
for _ in range(N+M):
    dict_people.append(sys.stdin.readline().rstrip())
set_seen = set(dict_people[:N])
set_heared = set(dict_people[N:])
set_seen_heared = list(set_seen & set_heared)
set_seen_heared.sort()

print(len(set_seen_heared))
for result in set_seen_heared:
    print(result)