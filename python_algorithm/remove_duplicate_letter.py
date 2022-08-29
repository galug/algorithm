import collections


def removeDuplicateLetters(s: str) -> str:
    stack = []
    counter = collections.Counter(s)
    for ch in s:
        counter[ch] -= 1
        while stack and stack[-1] > ch and counter[stack[-1]] > 0:
            stack.pop()
        if ch not in stack:
            stack.append(ch)
    return ''.join(stack)

s = "cbacdcbc"
print(removeDuplicateLetters(s))