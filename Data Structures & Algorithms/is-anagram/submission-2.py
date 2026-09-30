from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = defaultdict(int)
        t_counts = defaultdict(int)

        for c in s:
            s_counts[c] += 1
        
        for c in t:
            t_counts[c] += 1
        
        return all([s_counts[key] == t_counts.get(key, None) for key in s_counts])

        