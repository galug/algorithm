def dart_game(dartResult:str)->int:
    stack = []
    for ch in dartResult:
        if ch == 'S':
            stack[-1] **= 1
            stack.append()
        if dartResult[i] == '*':
            if len(stack)==1:
                stack[0] *=2
            else:
                if stack2:
                    if stack2[0] =='*':
                        stack[-1] *= 4
                        stack[-2] *= 4
                    elif stack2[0] == '#':
                        stack[-1] *= -2
                        stack[-2] *= -2
                else:
                    stack[-1]*=2
                    stack[-2]*=2
        if dartResult[i] == '#':
