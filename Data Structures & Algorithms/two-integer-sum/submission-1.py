class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap: key for element, value for index
        hashmap = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[nums[i]] = i

        
        return False # just for safety if no pair was found