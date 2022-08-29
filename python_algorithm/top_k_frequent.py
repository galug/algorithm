import collections

def topKFrequent(nums: [int], k: int) -> [int]:
    c = collections.Counter(nums)
    most_list = [ele[0] for ele in c.most_common(k)]
    return most_list
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))