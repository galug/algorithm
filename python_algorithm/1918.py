expression = input().rstrip()
op = []
str = ''
for ch in expression:
    if ch.isalpha():
        str += ch
    else:
        if ch == '(':
            op.append(ch)
        elif ch == ')':
            while op and op[-1] != '(':
                str += op.pop()
            op.pop()
        elif ch in '+-':
            while op and op[-1] != '(':
                str += op.pop()
            op.append(ch)
        else:
            while op and op[-1] in '*/':
                str += op.pop()
            op.append(ch)
while op:
    str += op.pop()
print(str)
