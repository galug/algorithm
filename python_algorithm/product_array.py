def productExceptSelf(nums: [int]) -> [int]:
    product_num = []
    p = 1
    for i in range(len(nums)):
        product_num.append(p)
        p*= nums[i]
    p = 1
    for i in range(len(nums)-1,0 - 1, -1):
        product_num[i] *= p
        p*= nums[i]
    return product_num
