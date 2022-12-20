import sys

line = sys.stdin.readline().rstrip().split()
base = line[0]
for i in range(1, len(line)):
    var = ''
    stack = []
    for ch in line[i]:
        if ch.isalpha():
            var += ch
        if ch in '&*':
            stack.append(ch)
        if ch in '[':
            stack.append('[]')
    result = base
    while stack:
        pop = stack.pop()
        result += pop
    result = result + ' ' + var + ';'
    print(result)