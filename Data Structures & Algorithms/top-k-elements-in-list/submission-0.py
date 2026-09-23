from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a hashmap for the num's frequency
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        # create output list
        sorted_counts = sorted(
            counts.items(), key= lambda item: item[1], reverse=True
        )
        top_k = [sorted_counts[i][0] for i in range(k)]

        return top_k
