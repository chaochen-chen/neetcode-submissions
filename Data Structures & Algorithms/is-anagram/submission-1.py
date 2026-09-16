from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = defaultdict(int)

        for c in s:
            hash_map[c] += 1
        
        for c in t:
            hash_map[c] -= 1
        
        return all(count == 0 for count in hash_map.values())