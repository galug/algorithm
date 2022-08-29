def threeSum(nums: [int]) -> [[int]]:
    results = []
    nums.sort()


    for i in range(len(nums) - 2):
        #delete overlap
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        #using two pointer
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                results.append([nums[i], nums[left], nums[right]])
                #delete overlap
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return results


