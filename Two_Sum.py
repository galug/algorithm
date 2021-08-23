def twoSum(nums, target: int):
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums[i+1:]:
                j = nums.index(complement)
                return [i, j]
print(twoSum([2,7,11,15],9))

