import collections

def is_palindrome_1(s: str) -> bool:
    n_s = ""
    # makes n_s from modified s
    for char in s:
        if char.isalnum():
            n_s+=char.lower()
    # if n_s is palindrome return True
    return n_s[::] == n_s[::-1]

def is_palindrome_2(s: str) -> bool:
    n_s : Deque = collections.deque()

    for char in s:
        if char.isalnum():
            n_s.append(s.lower())

    while len(n_s) > 1:
        if n_s.popleft() != n_s.pop():
            return False
    return True

print(is_palindrome_2("cda"))