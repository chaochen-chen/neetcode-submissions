from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a list with len 26 to record the count of chars of the strings
        # create a hashmap: key -> the tuple of count, value -> the list of anagram string
        hashmap = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                i = ord(c) - ord('a')
                count[i] += 1
            hashmap[tuple(count)].append(str)
        
        return list(hashmap.values())
            