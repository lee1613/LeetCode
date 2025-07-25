class Solution:
    def maxSum(self, nums: List[int]) -> int:
        

        unique_nums = set(nums)

        out = sum([i for i in unique_nums if i > 0])
        
        if out == 0:
            return max(unique_nums)

        return out
        