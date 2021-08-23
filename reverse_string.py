class Solution:
    def reverseString_1(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    def reverseString_2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # use built in function
        s.reverse()