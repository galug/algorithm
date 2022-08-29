def letterCombinations(digits: str) -> [str]:
    def dfs(result:str, k:int):
        if k == len(digits):
            results.append(result)
            return
        for ch in phone_dict[digits[k]]:
            dfs(result + ch, k+1)
    phone_dict = {
        '2' : ['a','b','c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r','s'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y','z']
    }
    results = []
    dfs("", 0)
    return results
pn = "23"
print(letterCombinations(pn))