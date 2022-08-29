class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        results = []
        def dfs(csum:int, result: list, start:int):
            if csum<0:
                return
            if csum==0:
                results.append(result)
                return
            else:
                for i in range(start, len(candidates)):
                    dfs(csum - candidates[i],result+[candidates[i]],i)
        dfs(target, [], 0)
        return results
s= Solution()
print(s.combinationSum([2,3,6,7],7))