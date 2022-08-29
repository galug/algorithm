def lengthOfLongestSubstring(s: str) -> int:
    max_len, start = 0, 0
    for i,ch in enumerate(s):
        if ch in s[start:i]:
            start = s[start:i].find(ch) + start + 1
            continue
        else:
            max_len = max(max_len, i - start + 1)
    return max_len