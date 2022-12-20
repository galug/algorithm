import sys

line = sys.stdin.readline()
stack = []

def bracket_calculate(bracket: str):
    result = 0
    tmp = 1
    for i in range(len(bracket)):
        if bracket[i] == '(':
            stack.append(bracket[i])
            tmp *= 2
        elif bracket[i] == '[':
            stack.append(bracket[i])
            tmp *= 3
        elif bracket[i] == ')':
            if not stack or stack[-1] != '(':
                return 0
            if bracket[i-1] == '(':
                result += tmp
            stack.pop()
            tmp = tmp // 2
        elif bracket[i] == ']':
            if not stack or stack[-1] != '[':
                return 0
            if bracket[i-1] == '[':
                result += tmp
            stack.pop()
            tmp = tmp // 3

    if stack:
        return 0
    else:
        return result

print(bracket_calculate(line))
