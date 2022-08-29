def permute(nums: [int]) -> [[int]]:
    if not nums:
        return []
    def dfs(result, k:int):
        if k== len(nums):
            results.append(result)
            return
        for num in nums:
            if num not in result:
                dfs(result+ [num], k+1)
    results = []
    dfs([],0)
    return results

def permute2(nums: [int]) -> [[int]]:
    if not nums:
        return []
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results


n_list = [1,2,3]
print(permute(n_list))
