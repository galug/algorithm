import sys
number_of_word = int(input())
words = [sys.stdin.readline().rstrip() for _ in range(number_of_word)]
answer = 0


words.sort(key = lambda word: len(word))
for i in range(number_of_word):
    is_prefix = False
    len_word = len(words[i])
    for j in range(i + 1, number_of_word):
        if words[i] in words[j][:len_word]:
            is_prefix = True
            break
    if not is_prefix:
        answer += 1
print(answer)
'''
number_of_word = int(input())
trie = {}
answer = 0

for _ in range(number_of_word):
    word = sys.stdin.readline().rstrip()
    t = trie
    is_not_in_trie = False
    included_trie = False
    for ch in word:
        if ch not in t:
            t[ch] = {}
            is_not_in_trie = True
        if '*' in t:
            included_trie = True
        t = t[ch]
    t['*'] = True
    if is_not_in_trie and not included_trie:
        answer += 1
print(answer)
'''