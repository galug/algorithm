def subsets(nums:[int]) -> [[int]]:
    results = []

    def dfs(index, path):
        results.append(path)

        for i in range(index, len(nums)):
            dfs(i+1, path+[nums[i]])
    dfs(0, [])
    return results
nums = [1,2,3]
print(subsets(nums))