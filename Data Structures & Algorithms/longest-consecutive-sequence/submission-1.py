class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set 
        # check whether num is the start of the seq
        # if num is the start, check num+1, num+2, ... exist
        num_sets = set(nums)
        max_len = 0
        for num in nums:
            seq_len = 1
            if num-1 not in num_sets: 
                while True:
                    if num+1 in num_sets:
                        seq_len += 1
                        num += 1
                    else:
                        break

            max_len = max(max_len, seq_len)
        
        return max_len



        