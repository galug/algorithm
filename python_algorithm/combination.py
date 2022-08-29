def combine(n: int, k: int) -> [[int]]:
    results = []
    def dfs(result:list, s:int):
        if len(result) == k:
            results.append(result)
            return
        for i in range(s, n + 1):
            dfs(result+[i],i+1)
    dfs([],1)
    return results

print(combine(4,2))