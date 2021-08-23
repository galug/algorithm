import collections
def groupAnagrams(strs):
    anagram = collections.defaultdict(list)

    # key = sorted(str) values= [str]
    for str in strs:
        anagram[''.join(sorted(str))].append(str)

    return list(anagram.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))