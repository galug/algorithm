import collections


def longestPalindrome(s: str) -> str:
    def expand(left:int, right:int) -> str:
        while left >=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    if len(s)<2 or s==s[::-1]:
        return s
    result= ""
    for i in range(len(s)-1):
        result = max(expand(i,i+1),expand(i,i+2),result,key=len)
    return result

str2 = longestPalindrome("abcbb")
print(str2)