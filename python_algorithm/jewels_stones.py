import collections
def numJewelsInStones(jewels: str, stones: str) -> int:
    c = collections.Counter(stones)
    j_num = 0
    for j in jewels:
        j_num += c[j]
    return j_num