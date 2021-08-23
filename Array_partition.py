class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        return sum(sorted(nums)[::2])