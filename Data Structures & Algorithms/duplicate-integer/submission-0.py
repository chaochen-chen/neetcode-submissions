class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set to record if an items has been seen
        # iterate the input list, once item is seen return True,
        # if finish iterating the list, return False
        seen = set()
        for item in nums:
            if item not in seen:
                seen.add(item)
            else:
                return True
        
        return False