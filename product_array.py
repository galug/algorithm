def productExceptSelf(nums: [int]) -> [int]:
    left_pro = []
    right_pro = []
    lp, rp = 1, 1
    # make from left to right product_array and make from right to left product_array
    for i in range(len(nums)):
        left_pro.append(lp)
        right_pro.append(rp)
        lp *= nums[i]
        rp *= nums[-(i+1)]
    # multiply left_pro to right_pro
    for i in range(len(nums)):
        left_pro[i] *= right_pro[-(i+1)]
    return left_pro

print(productExceptSelf([1, 2, 3, 4]))