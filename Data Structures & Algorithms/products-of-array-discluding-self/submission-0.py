class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix = [nums[0]] * len_nums
        postfix = [nums[-1]] * len_nums
        
        for i in range(1, len_nums):
            prefix[i] = nums[i] * prefix[i-1]
        for i in range(len_nums-2, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]
        
        outputs = []
        for i in range(len_nums):
            if i == 0:
                product = postfix[i+1]
            elif i == len_nums - 1:
                product = prefix[i-1]
            else:
                product = prefix[i-1] * postfix[i+1]
                
            outputs.append(product)
        
        return outputs