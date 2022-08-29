import collections

class Solution:
    def groupAnagrams(self, strs: chr) -> list(list):
        anagram_dict = collections.defaultdict(list)
        for str in strs:
            anagram_dict[''.join(sorted(str))].append(str)
        return list(anagram_dict.values())

