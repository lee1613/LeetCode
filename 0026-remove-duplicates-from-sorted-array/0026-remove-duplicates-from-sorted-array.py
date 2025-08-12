class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Must edit in place for all then numbers
        unique = sorted(set(nums))
        for i in range(len(unique)):
            nums[i] = unique[i]
        
        return len(unique)